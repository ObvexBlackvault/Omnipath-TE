from fastapi import APIRouter
from backend.core.ForkAlpha import ForkAlpha
from backend.core.ForkBeta import ForkBeta

status_router = APIRouter()

@status_router.get("/status")
def get_status():
    alpha_status = ForkAlpha.get_status()
    beta_status = ForkBeta.get_status()
    return {
        "ForkAlpha": alpha_status,
        "ForkBeta": beta_status
    }
