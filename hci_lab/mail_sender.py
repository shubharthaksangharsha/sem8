import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, sender_password):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
subject = "Test Email"
body = "This is a test email sent using Python."
sender_email = "shubharthaksangharsha@gmail.com"
receiver_email = "shubharthaksangharsha@gmail.com"
smtp_server = "smtp.gmail.com"  # SMTP server address
smtp_port = 587
sender_password = os.environ.get('myapp_pass')

send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, sender_password)
