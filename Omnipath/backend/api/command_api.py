from fastapi import APIRouter

command_router = APIRouter()

@command_router.post("/api/command")
async def handle_command(command: dict):
    # placeholder or real logic here
    return {"status": "received", "command": command}
