from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.CommandBridge import CommandBridge

command_router = APIRouter()

class CommandPayload(BaseModel):
    command: str

@command_router.post("/api/command")
async def handle_command(payload: CommandPayload):
    command = payload.command.strip().lower()

    try:
        result = CommandBridge.execute_command(command)
        return {"status": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Command execution failed: {str(e)}")
