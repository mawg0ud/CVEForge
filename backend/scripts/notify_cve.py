import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
import sqlite3

# Constants
PROCESSED_DATA_DIR = "backend/data/processed"
SIGNIFICANT_CVE_FILE = "significant_cve.json"
USER_DB = "backend/data/users.db"  # SQLite database for user preferences

# Function to load significant CVE data
def load_significant_cve_data():
    file_path = os.path.join(PROCESSED_DATA_DIR, SIGNIFICANT_CVE_FILE)
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to fetch user preferences from the database
def fetch_user_preferences():
    conn = sqlite3.connect(USER_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT email, software FROM user_preferences")
    user_preferences = cursor.fetchall()
    conn.close()
    return user_preferences

# Function to send email notifications
def send_email_notification(email, cve_list):
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    subject = "New Significant CVEs Related to Your Subscribed Software"
    body = "The following significant CVEs have been identified:\n\n"

    for cve in cve_list:
        body += f"CVE ID: {cve['CVE_ID']}\n"
        body += f"Description: {cve['Description']}\n"
        body += f"CVSS v3 Score: {cve['CVSS_v3_Score']}\n"
        body += f"CVSS v2 Score: {cve['CVSS_v2_Score']}\n"
        body += "\n"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

# Function to notify users of new significant CVEs
def notify_users():
    cve_data = load_significant_cve_data()
    user_preferences = fetch_user_preferences()

    for email, software in user_preferences:
        relevant_cves = [cve for cve in cve_data if software.lower() in cve['Description'].lower()]
        if relevant_cves:
            send_email_notification(email, relevant_cves)

if __name__ == "__main__":
    notify_users()
