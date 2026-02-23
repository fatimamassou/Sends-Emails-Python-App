# 📧 Bulk Email Sender (Python SMTP)

A simple Python script that sends emails with a PDF attachment (CV) to multiple recipients using Gmail SMTP.

This script reads email addresses from a text file and sends the same message and attachment to all recipients.



##  Features

- 📄 Reads recipient emails from a `.txt` file  
- 📎 Attaches a PDF file (e.g., CV)  
- 🔐 Secure connection using TLS  
- 📤 Sends emails in bulk via Gmail SMTP  



##  Built With

- Python 3  
- smtplib  
- ssl  
- email.message  



##  Project Structure

```
project-folder/
│
├── send_email.py
├── emails.txt
├── CV.pdf
└── README.md
```



##  Setup Instructions

### 1. Enable Gmail App Password

- Enable **2-Step Verification** in your Google account.
- Generate a **Gmail App Password**.
- Use the App Password inside the script.



### 2. Prepare `emails.txt`

Add one email per line:

```
example1@gmail.com
example2@gmail.com
example3@gmail.com
```



### 3. Configure the Script

Inside the Python file, update:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```



### 4. Run the Script

```bash
python send_email.py
```



##  Notes

- Do not use your real Gmail password always use an App Password.
- Gmail may temporarily block sending if too many emails are sent at once.
- This script sends the same message to all recipients.



##  Disclaimer

Use responsibly. Sending unsolicited bulk emails may violate email service policies.
