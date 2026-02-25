import smtplib
import ssl
import tkinter as tk
from tkinter import filedialog, messagebox
from email.message import EmailMessage


def browse_emails():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        emails_entry.delete(0, tk.END)
        emails_entry.insert(0, file_path)


def browse_cv():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        cv_entry.delete(0, tk.END)
        cv_entry.insert(0, file_path)


def send_emails():
    email_address = email_entry.get().strip()
    email_password = password_entry.get().strip()
    emails_file = emails_entry.get().strip()
    cv_file = cv_entry.get().strip()
    subject = subject_entry.get().strip()
    body = body_text.get("1.0", tk.END).strip()

    # Basic validation
    if not all([email_address, email_password, emails_file, cv_file, subject, body]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Load recipients
        with open(emails_file, "r") as f:
            recipients = [line.strip() for line in f if line.strip()]

        if not recipients:
            messagebox.showerror("Error", "Emails file is empty.")
            return

        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            smtp.login(email_address, email_password)

            sent_count = 0

            for recipient in recipients:
                msg = EmailMessage()
                msg["From"] = email_address
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.set_content(body)

                # Attach CV
                with open(cv_file, "rb") as cv:
                    msg.add_attachment(
                        cv.read(),
                        maintype="application",
                        subtype="pdf",
                        filename="CV.pdf"
                    )

                smtp.send_message(msg)
                sent_count += 1

        messagebox.showinfo(
            "Success",
            f"Emails sent successfully!\nTotal sent: {sent_count}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Bulk Email Sender")
root.geometry("520x520")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=30, pady=30)
main_frame.pack(fill="both", expand=True)

# Make columns expand properly
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)

# Email
tk.Label(main_frame, text="Your Email").grid(row=0, column=0, sticky="w", pady=(0, 5))
email_entry = tk.Entry(main_frame)
email_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))

# Password
tk.Label(main_frame, text="App Password").grid(row=2, column=0, sticky="w", pady=(0, 5))
password_entry = tk.Entry(main_frame, show="*")
password_entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 10))

# Emails file
tk.Label(main_frame, text="Emails File (.txt)").grid(row=4, column=0, sticky="w", pady=(0, 5))
emails_entry = tk.Entry(main_frame)
emails_entry.grid(row=5, column=0, sticky="ew", pady=(0, 10))
tk.Button(main_frame, text="Browse", command=browse_emails).grid(row=5, column=1, padx=5)

# CV file
tk.Label(main_frame, text="CV File (.pdf)").grid(row=6, column=0, sticky="w", pady=(0, 5))
cv_entry = tk.Entry(main_frame)
cv_entry.grid(row=7, column=0, sticky="ew", pady=(0, 10))
tk.Button(main_frame, text="Browse", command=browse_cv).grid(row=7, column=1, padx=5)

# Subject
tk.Label(main_frame, text="Subject").grid(row=8, column=0, sticky="w", pady=(0, 5))
subject_entry = tk.Entry(main_frame)
subject_entry.grid(row=9, column=0, columnspan=2, sticky="ew", pady=(0, 10))

# Message
tk.Label(main_frame, text="Message").grid(row=10, column=0, sticky="w", pady=(0, 5))
body_text = tk.Text(main_frame, height=6)
body_text.grid(row=11, column=0, columnspan=2, sticky="ew", pady=(0, 15))

# Send button
tk.Button(
    main_frame,
    text="Send Emails",
    bg="blue",
    fg="white",
    command=send_emails
).grid(row=12, column=0, columnspan=12, pady=(0, 10))

root.mainloop()