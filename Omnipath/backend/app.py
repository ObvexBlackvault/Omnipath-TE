from fastapi import FastAPI
from backend.api.status_api import status_router
# other imports...

app = FastAPI()

app.include_router(status_router, prefix="/api")
# other routers...
