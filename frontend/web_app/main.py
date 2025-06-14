# frontend/web_app/main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes import student_routes

app = FastAPI()
app.include_router(student_routes.router)

app.mount("/static", StaticFiles(directory="frontend/web_app/static"), name="static")
templates = Jinja2Templates(directory="frontend/web_app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
