import time
import os

from flask import Flask, redirect, request, session, jsonify
from firebase import auth
from flask_cors import CORS
from flask_session import Session

from werkzeug.utils import secure_filename

from DbManager import DbManager
from FlashcardChat import FlashcardChat
from StudyGroup import StudyGroup

app = Flask(__name__, static_folder='../build', static_url_path='/')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super sdfsdfhsidfuhsijdfhskdjfskfhksfhkshfksdhfkjecret key'

Session(app)
CORS(app)

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/api/login",methods=["POST","GET"])
def login():
    if request.method =="POST":
        
        result=request.form
        email=result["email"]
        password=result["pass"]
        try:
            #Try signing in the user with the given information
            user = auth.sign_in_with_email_and_password(email, password)
            
            #insert the user information into the session
            session["is_logged_in"] = True
            session["email"] = user["email"]
            session["uid"] = user["localId"]
            session["user"] = user
            
            #Get the name of the user
            session["name"] = user["displayName"] or email
            return redirect('/')
        except Exception as e:
            return redirect('/api/login')
    else:
        if session.get("user",False):
            return {'loggedIn':True}
        return {'loggedIn':False}

@app.route("/api/register",methods=["POST","GET"])
def register():
    if request.method =="POST":
        result=request.form
        email=result["email"]
        password=result["pass"]
        password2=result["pass2"]
        if password!=password2: return redirect('/api/register')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            return redirect('/api/login')	
        except Exception as e:
            print(e)
            return redirect('/api/register')
    else:
        return {'loggedIn':True}

@app.route("/api/forgot",methods=["POST","GET"])
def forgotPassword():
    if request.method =="POST":
        result=request.form
        email=result["email"]
        try:
            #send recovery email
            auth.send_password_reset_email(email)
            return redirect('/login')
        except Exception as e:
            return redirect('/forgot')
    else:
        return {'loggedIn':True}

db_manager = DbManager()
db_manager.create_tables()
flashcard_chat = FlashcardChat()

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/deck', methods=['POST'])
def create_deck():
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401

    text_input = None
    if 'input' in request.json:
        text_input = request.json['input']
    elif 'image' in request.files:
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            text_input = get_text_from_image(file.filename, file_path)
            if not text_input:
                return jsonify({'error': 'Unable to extract text from image'}), 400
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
    else:
        return jsonify({'error': 'Missing required fields'}), 400

    response = create_deck_from_text(text_input)
    return jsonify(response), 201 if 'deck_id' in response else 400

def get_text_from_image(image_name, image_path):
    try:
        return flashcard_chat.readImage(image_name, image_path)
    except Exception as e:
        print(f"Error reading image: {e}")
        return None

def create_deck_from_text(text_input):
    # Generate title and description using Claude 3.5 API
    title_description_response = flashcard_chat.getTitleAndDescription(text_input)
    title_description_lines = title_description_response.split('\n\n')
    title = title_description_lines[0].replace("Title: ", "").strip()
    description = title_description_lines[1].replace("Description: ", "").strip()
    
    # Create the deck
    deck_id = db_manager.add_deck(session["uid"], title, description)

    # Generate flashcards using Claude 3.5 API
    flashcards_text = flashcard_chat.createFlashcard(text_input)
    
    # Process the flashcards and add them to the deck
    flashcards = flashcards_text.split('\n\n')
    for flashcard in flashcards:
        if '|||' in flashcard:
            concept, detail = flashcard.split('|||')
            db_manager.add_card(deck_id, concept.strip(), detail.strip())

    return {
        'message': 'Deck created successfully',
        'deck_id': deck_id
    }

@app.route('/api/feedback', methods=['POST'])
def provide_feedback():
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401

    data = request.json
    if not data or 'card_concept' not in data or 'card_detail' not in data or 'user_response' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    card_concept = data['card_concept']
    card_detail = data['card_detail']
    user_response = data['user_response']

    # Get feedback using Claude 3.5 API
    feedback = flashcard_chat.feedback(card_concept, card_detail, user_response)

    return jsonify({
        'feedback': feedback
    }), 200

@app.route('/api/decks', methods=['GET'])
def get_user_decks():
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401
    decks = db_manager.get_decks_with_count(session["uid"])
    return jsonify(decks)

@app.route('/api/deck/<int:deck_id>/cards', methods=['GET'])
def get_deck_cards(deck_id):
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401
    cards = db_manager.get_cards_by_deck_id(deck_id, session["uid"])
    if cards is None:
        return jsonify({'error': 'Deck not found or access denied'}), 404
    return jsonify(cards)

@app.route('/api/deck/<int:deck_id>', methods=['GET'])
def get_deck(deck_id):
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401
    deck = db_manager.get_deck(deck_id)
    if deck is None:
        return jsonify({'error': 'Deck not found or access denied'}), 404
    return jsonify(deck)

@app.route('/api/conversation/characters', methods=['GET'])
def get_characters():
    return jsonify(StudyGroup.characters), 200

@app.route('/api/conversation/create', methods=['POST'])
def create_conversation():
    data = request.json
    if "deck_id" not in data or "characters" not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    deck_id = data["deck_id"]
    characters = data["characters"]
    deck = db_manager.get_deck(deck_id)

    if deck is None:
        return jsonify({'error': 'Deck not found or access denied'}), 404

    if not session.get("conversation"):
        session["conversation"] = {}

    def format_flashcards(data):
        cards = data.get("cards", [])
        formatted_cards = []
        for card in cards:
            concept = card.get("concept", "")
            detail = card.get("detail", "")
            formatted_cards.append(f"{concept}|||{detail}")
        return formatted_cards

    deck_string = format_flashcards(deck)

    # Can overwrite the last conversation of the deck if you want to select new characters
    session["conversation"][deck_id] = StudyGroup(deck_string, characters)

    return jsonify({
        'message': 'Conversation created successfully',
        'deck_id': deck_id
    }), 201


@app.route('/api/conversation/<int:deck_id>', methods=['POST'])
def get_new_message(deck_id):
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401
    
    data = request.json
    deck = db_manager.get_deck(deck_id)

    if 'input' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    if deck is None:
        return jsonify({'error': 'Deck not found or access denied'}), 404

    if not session.get("conversation") or deck_id not in session["conversation"]:
        return jsonify({'error': 'Conversation not found or access denied'}), 404
    
    group = session["conversation"][deck_id]
    return jsonify(group.userMessage(data['input']))

