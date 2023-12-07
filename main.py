from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.note_routes import router as note_router

load_dotenv()

app = FastAPI()

app.include_router(note_router, prefix='/api/v1/notes')