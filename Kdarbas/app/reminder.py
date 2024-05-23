from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import schedule
import time
from datetime import date

from sqlalchemy import extract
import database as data
import models as mod
import smtplib
from email.mime.text import MIMEText

app = FastAPI()


def send_email(From: str, to: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = From
    msg['To'] = to

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)


def check_birthdays():
    try:
        db = data.Database().get_db()
        today = date.today()

        birthdays = db.query(mod.Birthday).filter(
            (extract('month', mod.Birthday.B_date) == today.month) &
            (extract('day', mod.Birthday.B_date) == today.day)
        ).all()

        for birthday in birthdays:
            user = db.query(mod.User).filter(mod.User.id == birthday.user_id).first()
            if user:
                send_email(mod.User.Email, mod.User.Email, "Birthday Reminder", f"Today is {birthday.Name}'s birthday!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db.close()

schedule.every().day.at("08:00").do(check_birthdays)


@app.post("/check-birthdays/")
async def run_check_birthdays():
    try:
        check_birthdays()
        return JSONResponse(content={"message": "Birthday reminders sent successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
