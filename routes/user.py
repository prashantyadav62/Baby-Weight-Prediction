from flask import Blueprint

## creating a blueprint/mini flask app for predict object

user_bp = Blueprint("user", __name__)




##ROUTES FOR USER

@user_bp.route('/get-user', methods=['GET'])
def get_user():
    return "This is GET user route"

@user_bp.route('/update-user', methods=['PUT'])
def update_user():
    return "This is UPDATE user route"

@user_bp.route('/create-user', methods=['POST'])
def create_user():
    return "This is CREATE user route"

@user_bp.route('/delete-user', methods=['DELETE'])
def delete_user():
    return "This is DELETE user route"