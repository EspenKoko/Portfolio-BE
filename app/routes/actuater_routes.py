from flask import Blueprint, jsonify

actuater_bp = Blueprint("actuater", __name__)

@actuater_bp.route("/health", methods=["GET"])
def get_health():
    return jsonify({"status": "ok"})