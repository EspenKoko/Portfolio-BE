from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..models.user import User
from ..schemas.user_schema import UserSchema
# from marshmallow import ValidationError
# from ..utils import exception_util, service_util
# from ..exceptions.service_exception import ServiceException
# from api.constant.message_code import MessageCode
# from ..services.user_service import UserService

user_bp = Blueprint("user", __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@swag_from('../../docs/user.yml')
@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    print(users)
    print(users_schema.dump(users))
    return users_schema.jsonify(users)

@user_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    """
    Get a user by ID
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: User object
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@user_bp.route("/new", methods=["POST"])
def create_user():
    data = request.get_json()
    
    try:
        new_user = User(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            location=data.get("location"),
            summary=data.get("summary"),
            profile_picture=data.get("profile_photo")
        )
        from .. import db
        db.session.add(new_user)
        db.session.commit()
        # validatedData = user_schema().load(data)
        # user = User(**validatedData)
        # msg = UserService().consume(user)
        # return service_util.build_server_response(MessageCode.SUCCESS, msg)

        return user_schema.jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    # except (ValidationError, ServiceException) as err:
    #     return exception_util.handler(err)