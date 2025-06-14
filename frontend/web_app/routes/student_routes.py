# frontend/web_app/routes/student_routes.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="frontend/web_app/templates")
router = APIRouter()

@router.post("/start-quiz", response_class=HTMLResponse)
def start_quiz(request: Request, student_id: str = Form(...)):
    return templates.TemplateResponse("quiz.html", {"request": request, "student_id": student_id})

@router.post("/submit-quiz", response_class=HTMLResponse)
def submit_quiz(request: Request, student_id: str = Form(...), q1: str = Form(...), q2: str = Form(...)):
    # mock analysis result
    weaknesses = ["Quadratic Factoring"] if q1 != "B" else []
    return templates.TemplateResponse("learning_path.html", {
        "request": request,
        "student_id": student_id,
        "topics": weaknesses
    })
