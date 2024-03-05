import requests
import hashlib
import time
import smtplib
from email.mime.text import MIMEText

# URL of the website to monitor
url = "https://mattheusstearns.com"

# Initial content hash (you can set it to None for the first run)
previous_hash = None

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "websitescroller@gmail.com"
receiver_email = "websitescroller@gmail.com"
email_password = "The Matt#1549"

while True:
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()

        # Calculate the content hash of the response
        current_hash = hashlib.sha256(response.content).hexdigest()

        if previous_hash is None:
            # Store the initial content hash
            previous_hash = current_hash
        elif current_hash != previous_hash:
            # Website has been updated, send email notification
            message = MIMEText("The website has been updated!")
            message["Subject"] = "Website Update Notification"
            message["From"] = sender_email
            message["To"] = receiver_email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, email_password)
                server.send_message(message)

            # Update the previous hash with the new one
            previous_hash = current_hash

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

    # Wait for a specified time before checking again (e.g., 1 hour)
    time.sleep(60)
