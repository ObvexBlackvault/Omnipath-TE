from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.CommandBridge import CommandBridge

command_router = APIRouter()
bridge = CommandBridge()

class Payload(BaseModel):
    command: str

@command_router.post("/api/command")
async def handle_command(payload: Payload):
    result = bridge.handle_command(payload.command)
    return result
