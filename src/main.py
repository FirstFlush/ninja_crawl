from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .routes import router
from .config import ENV, setup_logging

setup_logging(env=ENV)

app = FastAPI()
app.include_router(router)
