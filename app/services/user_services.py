from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.extensions import db
from marshmallow import ValidationError

from flask import abort
from app.models.user import User
from app.schemas.user_schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)
update_schema = UserSchema(partial=True)

def getAllUsers() -> object:
    users: list[User] | None = User.query.all()
    return users_schema.jsonify(users)

def getUserByEmail(email: str) -> object:
    user = User.query.filter_by(email=email).first()
    if not user:
        abort(404, description="User not found")
    return user_schema.jsonify(user)

def createUser(newUserData: dict) -> object:
    user: User | None = User.query.filter_by(email=newUserData.get("email")).first()
    if user:
        abort(409, description="User with this email already exists")
        
    newUser: User = User()
    
    print("[create_user] Fields to create:")
    for key, value in newUserData.items():
        if hasattr(newUser, key):
            print(f"  - {key}: {value}")
            setattr(newUser, key, value)
        else:
            print(f"  - {key}: not a valid field on User, skipping.")
            
    db.session.add(newUser)
    try:
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        abort(500, description=str(err))
        
    return user_schema.jsonify(newUser)

def updateUser(userEmail: str, updatedUserData: dict) -> dict:
    errors = update_schema.validate(updatedUserData)
    if errors:
        print("[update_user] Validation error:", errors)
        return {"success": False, "errors": errors}

    user = User.query.filter_by(email=userEmail).first()
    if not user:
        return {"success": False, "errors": "User not found."}

    print("[update_user] Fields to update:")
    for key, value in updatedUserData.items():
        if hasattr(user, key):
            old_value = getattr(user, key, None)
            print(f"  - {key}: {old_value} -> {value}")
            setattr(user, key, value)
        else:
            print(f"  - {key}: not a valid field on User, skipping.")

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"[update_user] Error during commit: {e}")
        return {"success": False, "errors": str(e)}

    result = update_schema.dump(user)
    return {"success": True, "user": result}