from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Depends, HTTPException
from pydantic import BaseModel, EmailStr, constr
from fastapi import FastAPI, HTTPException, Request
from sendEmail import send_email






app = FastAPI()

templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("usage.html", {"request": request})

class EmailPayload(BaseModel):
    subject: constr(strip_whitespace=True, min_length=1)
    message: constr(strip_whitespace=True, min_length=1)
    receiver: EmailStr

@app.post("/send-email")
async def send_email_endpoint(payload: EmailPayload):
    try:
        await send_email(
            receiver_email=payload.receiver,
            subject=payload.subject,
            body=payload.message
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "success", "detail": "Email sent"}
