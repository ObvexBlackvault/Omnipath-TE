def validate_mission_payload(mission: dict) -> bool:
    """
    Validate that the incoming mission payload contains the required fields.

    Expected structure:
    {
        "command": "string",
        "message": "string"
    }

    Returns True if valid, raises ValueError if invalid.
    """
    if not isinstance(mission, dict):
        raise ValueError("Mission must be a dictionary.")

    if "command" not in mission or not isinstance(mission["command"], str):
        raise ValueError("Mission must include a 'command' string.")

    if "message" not in mission or not isinstance(mission["message"], str):
        raise ValueError("Mission must include a 'message' string.")

    return True


# ✅ Provide alternate name for compatibility
validate_mission = validate_mission_payload
