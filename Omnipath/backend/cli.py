from fastapi import FastAPI
from backend.api.command_api import command_router
from backend.api.status_api import status_router

app = FastAPI()

app.include_router(command_router, prefix="/api")
app.include_router(status_router, prefix="/api")
