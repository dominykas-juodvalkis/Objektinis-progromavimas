import schedule
import time
from datetime import date
from database import Database
from models import Birthday, User
import smtplib
from email.mime.text import MIMEText

def send_email(From: str, to: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = From
    msg['To'] = to

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)

def check_birthdays():
    db = next(Database().get_db())
    today = date.today()
    birthdays = db.query(Birthday).filter(Birthday.date == today).all()
    for birthday in birthdays:
        user = db.query(User).filter(User.id == birthday.user_id).first()
        if user:
            send_email(user.email, user.email, "Birthday Reminder", f"Today is {birthday.name}'s birthday!")
    db.close()

schedule.every().day.at("08:00").do(check_birthdays)

while True:
    schedule.run_pending()
    time.sleep(60)
