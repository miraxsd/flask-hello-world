from flask import Blueprint, request, jsonify
from .models import User, Subscription, db
from .utils import create_user, authenticate_user, check_subscription_status

routes = Blueprint('routes', __name__)

@routes.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user = create_user(data)
    if user:
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
    return jsonify({"message": "User registration failed"}), 400

@routes.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data)
    if user:
        return jsonify({"message": "Login successful", "token": user.generate_token()}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@routes.route('/api/subscription', methods=['POST'])
def subscribe():
    data = request.json
    user_id = data.get('user_id')
    plan_id = data.get('plan_id')
    
    subscription = Subscription(user_id=user_id, plan_id=plan_id)
    db.session.add(subscription)
    db.session.commit()
    
    return jsonify({"message": "Subscription created successfully", "subscription_id": subscription.id}), 201

@routes.route('/api/subscription/status', methods=['GET'])
def subscription_status():
    user_id = request.args.get('user_id')
    subscription = check_subscription_status(user_id)
    
    if subscription:
        return jsonify({"status": subscription.status}), 200
    return jsonify({"message": "No active subscription found"}), 404

@routes.route('/api/logout', methods=['POST'])
def logout():
    # Logic to invalidate user session/token
    return jsonify({"message": "Logout successful"}), 200