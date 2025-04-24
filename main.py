from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException , Request
import re

app = FastAPI()

@app.post("/send-email")
async def send_email_endpoint(request: Request):

    payload = await request.json()

    subject = payload.get("subject")
    message = payload.get("message")
    receiver = payload.get("receiver")

    if not subject or not message or not receiver:
        raise HTTPException(status_code=400, detail="Subject, message, and receiver are required")

    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", receiver):
        raise HTTPException(status_code=400, detail="Invalid email address format")

    try:
        return {"status": "success", "detail": "Email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("usage.html", {"request": request})