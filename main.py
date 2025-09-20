import smtplib
import ssl
from email.message import EmailMessage

# Your email credentials
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Gmail App Password

# Load emails from file
with open("emails.txt", "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

# Email content
subject = "Application for a Job Opportunity"
body = "body"

# Create SSL context
context = ssl._create_unverified_context()

# Send emails
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)   # Upgrade to secure connection
    smtp.ehlo()   # send email here
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for recipient in recipients:
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach CV
        with open("CV.pdf", "rb") as cv:
            msg.add_attachment(
                cv.read(),
                maintype="application",
                subtype="pdf",
                filename="CV.pdf"
            )

        smtp.send_message(msg)

print("✅ Emails sent successfully to all recipients!")
