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
body = """\
Dear Hiring Manager,

I am reaching out to express my interest in job opportunities at your company.
Please find attached my CV for your consideration.

Best regards,
[Your Name]
"""

# Send emails
for recipient in recipients:
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach CV
    with open("CV.pdf", "rb") as cv:
        msg.add_attachment(cv.read(), maintype="application", subtype="pdf", filename="CV.pdf")

    # Send
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

print("✅ Emails sent successfully to all 5 recipients!")
