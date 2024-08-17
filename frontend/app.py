import logging
from fetch_cve import fetch_cve_data
from analyze_cve import analyze_cve_data, load_raw_data, save_analyzed_data
from notify_cve import notify_users
import config

# Setup logging
logging.basicConfig(
    filename=config.LOG_FILE,
    level=getattr(logging, config.LOG_LEVEL.upper(), logging.INFO),
    format='%(asctime)s %(levelname)s %(message)s'
)

def main():
    logging.info("Starting CVE data fetch process...")
    try:
        fetch_cve_data()
        logging.info("CVE data fetch process completed successfully.")
    except Exception as e:
        logging.error(f"Error during CVE data fetch: {e}")
        return

    logging.info("Starting CVE data analysis process...")
    try:
        raw_data = load_raw_data()
        significant_cve_data = analyze_cve_data(raw_data)
        save_analyzed_data(significant_cve_data)
        logging.info("CVE data analysis process completed successfully.")
    except Exception as e:
        logging.error(f"Error during CVE data analysis: {e}")
        return

    logging.info("Starting CVE notification process...")
    try:
        notify_users()
        logging.info("CVE notification process completed successfully.")
    except Exception as e:
        logging.error(f"Error during CVE notification: {e}")

if __name__ == "__main__":
    main()
