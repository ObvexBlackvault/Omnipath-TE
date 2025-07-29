from fastapi import FastAPI
from backend.api.command_api import command_router
from backend.api.status_api import status_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Omnipath Backend API is live"}

# These must be registered
app.include_router(command_router)
app.include_router(status_router)
