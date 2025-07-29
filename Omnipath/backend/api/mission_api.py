from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.ForkFleetController import ForkFleetController

router = APIRouter()
fleet = ForkFleetController()

class MissionRequest(BaseModel):
    agent: str
    path: str

@router.post("/api/mission")
def trigger_mission(request: MissionRequest):
    result = fleet.execute_mission(request.agent, request.path)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/api/mission/all")
def trigger_all_missions(request: MissionRequest):
    result = fleet.assign_all(request.path)
    return result
