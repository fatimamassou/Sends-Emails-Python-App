# 📧 Bulk Email Sender (Python SMTP + Tkinter GUI)

A Python application that sends emails with a PDF attachment (CV) to multiple recipients using Gmail SMTP.

This project includes:

-  A CLI (script-based) version  
-  A Tkinter desktop GUI version  

Both versions send the same message and attachment to multiple recipients listed in a `.txt` file.



##  Features

- 📄 Reads recipient emails from a `.txt` file  
- 📎 Attaches a PDF file (e.g., CV)  
- 🔐 Secure connection using TLS  
- 📤 Sends emails in bulk via Gmail SMTP  
- 🖥️ Desktop interface built with Tkinter (GUI version)



## 🛠 Built With

- Python 3  
- smtplib  
- ssl  
- email.message  
- Tkinter  



## 📂 Project Structure

```
bulk-email-sender/
│
├── cli_version/
│   └── send_email.py
│
├── tkinter_version/
│   └── app.py
│
├── emails.txt
├── CV.pdf
└── README.md
```



# 🖥️ Version 1: CLI (Script Version)

A simple terminal-based script.

## ▶ How to Run

```bash
python send_email.py
```

Make sure to configure inside the script:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```



# 🪟 Version 2: Tkinter GUI Version

A desktop interface that allows you to:

- Enter your email and app password  
- Select the emails file using file browser  
- Select the CV PDF file  
- Write subject and message  
- Send emails with one click  

## ▶ How to Run

```bash
python app.py
```



## ⚙️ Setup Instructions

### 1. Enable Gmail App Password

- Enable **2-Step Verification** in your Google account  
- Generate a **Gmail App Password**  
- Use the App Password (not your real Gmail password)



### 2. Prepare `emails.txt`

Add one email per line:

```
example1@gmail.com
example2@gmail.com
example3@gmail.com
```



## ⚠️ Notes

- Never use your real Gmail password always use an App Password  
- Gmail may temporarily block sending if too many emails are sent at once  
- This app sends the same message to all recipients  
- Sending limits depend on your Gmail account type  



## ⚠️ Disclaimer

Use responsibly. Sending unsolicited bulk emails may violate email service policies and anti-spam laws.
