from fastapi import APIRouter

status_router = APIRouter()

@status_router.get("/status")
async def get_status():
    return {"status": "All systems nominal"}
