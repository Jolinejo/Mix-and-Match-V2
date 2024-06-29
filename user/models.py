from flask import jsonify, request, session
import uuid
import bcrypt
from extensions import db, app
from sqlalchemy.dialects.postgresql import JSON
import json

class User(db.Model):
    """User class with user funcitons for the routes"""
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(128), nullable=False)
    season = db.Column(db.String(50))
    matching_colors = db.Column(JSON)
    best_hair_color = db.Column(JSON)

    def start_session(self, user):
        """starts a session and removes the password"""
        session['logged_in'] = True
        session['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        print(session)
        return jsonify(session['user']), 200
    
    def sign_up(self):
        """signs up a user and starts the session"""
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400
        new_user = User(username=username, email=email, password=hashed_password)        
        db.session.add(new_user)
        db.session.commit()
        return new_user.start_session(new_user)
    
    def signout(self):
        """clears the session to sign out the user"""
        session.clear()
        return jsonify({"message": "signed out"}), 200
    
    def update_user(self):
        """updates the user based on sent keys and values"""
        data = request.json
        user_id = session['user']['id']

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        for key, value in data.items():
            if key == "matchingColors":
                key = "matching_colors"
            if key == "bestHairColors":
                key = "best_hair_color"
            setattr(user, key, value)
        
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    
    def get_user_data(self):
        """retrieves user data based on query keys"""
        keys = request.args.getlist('keys')
        if 'user' not in session:
            return jsonify({"error": "User not logged in"}), 401

        user_id = session['user']['id']

        user = User.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        user_data = {}
        for key in keys:
            if key == "matchingColors":
               key = "matching_colors"
            value = getattr(user, key)
            user_data[key] = value

        return jsonify(user_data), 200
    
    
    def login(self):
        """logs in user and starts the session"""
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            print(user)
            return self.start_session(user)
        
        return jsonify({ "error": "Invalid login credentials" }), 401

with app.app_context():
    db.create_all()
