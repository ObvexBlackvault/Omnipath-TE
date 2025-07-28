
from flask import Blueprint, jsonify
from CoreStatus import CoreStatus

status_api = Blueprint("status_api", __name__)
status = CoreStatus()

@status_api.route("/api/status", methods=["GET"])
def get_status():
    return jsonify({"log": status.get_log()})
