from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()

from routes.objectRoutes import router as objectRouter

app = FastAPI()

api_app = FastAPI()

origins = os.getenv("CORS_ORIGINS").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
api_app.include_router(router=objectRouter, tags=["Object"], prefix="/object")


app.mount("/api", api_app, name="api")

app.mount("/", StaticFiles(directory="../build", html=True), name="build")

templates = Jinja2Templates(directory="../build")


@app.exception_handler(404)
async def catch_all(request: Request, exc: HTTPException):
    return templates.TemplateResponse("index.html", {"request": request})
