from dotenv import load_dotenv 
import smtplib, ssl, os, asyncio



load_dotenv()


load_dotenv()
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
context = ssl.create_default_context()

async def send_email(receiver_email: str, subject: str, body: str):
    server = None
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls(context=context)
        server.login(SMTP_USER, SMTP_PASS)
        message = f"Subject: {subject}\n\n{body}"
        await asyncio.sleep(0)
        server.sendmail(SMTP_USER, receiver_email, message)
    finally:
        if server:
            server.quit()
