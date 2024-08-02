import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# CVE Data Fetching
NVD_API_URL = os.getenv("NVD_API_URL", "https://services.nvd.nist.gov/rest/json/cves/1.0")
RESULTS_PER_PAGE = int(os.getenv("RESULTS_PER_PAGE", 2000))
DATE_FORMAT = os.getenv("DATE_FORMAT", "%Y-%m-%dT%H:%M:%S:%fZ")

# Directories
RAW_DATA_DIR = os.getenv("RAW_DATA_DIR", "backend/data/raw")
PROCESSED_DATA_DIR = os.getenv("PROCESSED_DATA_DIR", "backend/data/processed")
SIGNIFICANT_CVE_FILE = os.getenv("SIGNIFICANT_CVE_FILE", "significant_cve.json")

# User Preferences Database
USER_DB = os.getenv("USER_DB", "backend/data/users.db")

# Email Notifications
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your_email@example.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_email_password")
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@example.com")

# Logging Configuration
LOG_FILE = os.getenv("LOG_FILE", "backend/logs/app.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
