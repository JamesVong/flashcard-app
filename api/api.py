import time
from flask import Flask, redirect, request, session, jsonify
from firebase import auth
from flask_cors import CORS
from flask_session import Session

from DbManager import DbManager
from FlashcardChat import FlashcardChat

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

@app.route('/api/deck', methods=['POST'])
def create_deck():
    if not session.get("uid"):
        return jsonify({'error': 'User not logged in'}), 401
    
    data = request.json
    if not data or 'name' not in data or 'input' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Generate title and description using Claude 3.5 API
    title_description_response = flashcard_chat.getTitleAndDescription(data['input'])
    title_description_lines = title_description_response.split('\n\n')
    title = title_description_lines[0].replace("Title: ", "").strip()
    description = title_description_lines[1].replace("Description: ", "").strip()
    
    # Create the deck
    deck_id = db_manager.add_deck(session["uid"], title, description)

    # Generate flashcards using Claude 3.5 API
    flashcards_text = flashcard_chat.createFlashcard(data['input'])
    
    # Process the flashcards and add them to the deck
    flashcards = flashcards_text.split('\n\n')
    for flashcard in flashcards:
        if '|||' in flashcard:
            concept, detail = flashcard.split('|||')
            db_manager.add_card(deck_id, concept.strip(), detail.strip())

    return jsonify({
        'message': 'Deck created successfully',
        'deck_id': deck_id
    }), 201

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
