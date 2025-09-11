from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.user_services import updateUser, createUser, getUserByEmail, getAllUsers
# from marshmallow import ValidationError

user_bp = Blueprint("user", __name__)

@swag_from('../../docs/user.yml')
@user_bp.route("/", methods=["GET"])
def get_users():
    users = getAllUsers()
    return users

@user_bp.route("/<string:email>", methods=["GET"])
def get_user(email):
    """
    Get a user by email
    ---
    parameters:
      - in: path
        name: email
        required: true
        type: string
    responses:
      200:
        description: User object
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    user = getUserByEmail(email)
    return user

@user_bp.route("/new", methods=["POST"])
def create_user():
    data = request.get_json()
    
    # Todo this conflict with the error handling in createApp
    new_user = createUser(data)
    return new_user, 201
  
@user_bp.route("/<string:email>", methods=["PUT"])
def update_user_route(email):
    """
    Update a user by email
    ---
    parameters:
      - in: path
        name: email
        required: true
        type: string
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/User'
    responses:
      200:
        description: User updated successfully
        schema:
          $ref: '#/definitions/User'
      400:
        description: Validation error or bad request
      404:
        description: User not found
    """
    data = request.get_json()
    if not data: # TODO this doesnt work
        return jsonify({"success": False, "errors": "No input data provided."}), 400

    result = updateUser(email, data)
    if not result.get("success"):
        errors = result.get("errors", "Unknown error")
        status_code = 404 if errors == "User not found." else 400
        return jsonify({"success": False, "errors": errors}), status_code

    return jsonify(result["user"]), 200