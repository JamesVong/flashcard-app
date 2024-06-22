import time
from flask import Flask, redirect, request, session
from firebase import auth
from flask_cors import CORS
from flask_session import Session

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
            return redirect('/login')
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
        if password!=password2: return redirect('/register')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            return redirect('/login')	
        except Exception as e:
            return redirect('/register')
    else:
        return {'loggedIn':True}

@app.route("/api/forgot",methods=["POST","GET"])
def frogotPassword():
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