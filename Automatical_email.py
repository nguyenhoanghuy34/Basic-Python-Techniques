import smtplib
from email.message import EmailMessage

EMAIL_SENDER = "nguyenhoanghuy@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "someone@example.com"

def send_email(subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Đã gửi:", subject)

for i in range(1, 11):
    subject = f"Mail thứ {i}"
    content = f"Đây là mail thứ {i} được gửi tự động."
    send_email(subject, content)
