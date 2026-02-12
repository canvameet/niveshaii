from flask import Flask, render_template, session, redirect, url_for, request, jsonify
import os
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')

# Secret key for session management from environment variable
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login')
def login():
    # If already logged in, redirect to main page
    if 'user_id' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/verify-token', methods=['POST'])
def verify_token():
    """Verify Firebase token and create session"""
    try:
        data = request.get_json()
        user_id = data.get('uid')
        email = data.get('email')
        
        if user_id and email:
            # Create session
            session['user_id'] = user_id
            session['email'] = email
            return jsonify({'success': True})
        
        return jsonify({'success': False, 'error': 'Invalid token'}), 401
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/firebase-config', methods=['GET'])
def get_firebase_config():
    """Serve Firebase configuration from environment variables"""
    config = {
        'apiKey': os.environ.get('FIREBASE_API_KEY'),
        'authDomain': os.environ.get('FIREBASE_AUTH_DOMAIN'),
        'projectId': os.environ.get('FIREBASE_PROJECT_ID'),
        'storageBucket': os.environ.get('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.environ.get('FIREBASE_APP_ID'),
        'measurementId': os.environ.get('FIREBASE_MEASUREMENT_ID')
    }
    return jsonify(config)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':  
    print("="*70)
    print("NIVESHAI - FRONTEND SERVER")
    print("="*70)
    print("Frontend running on: http://localhost:8080")
    print("Make sure backend API is running on: http://localhost:5000")
    print("="*70 + "\n")
    
    import webbrowser
    try:
        webbrowser.open('http://localhost:8080')
    except:
        pass
    
    app.run(debug=True, host='0.0.0.0', port=8080)