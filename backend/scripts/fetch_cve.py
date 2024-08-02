import requests
import json
import os
from datetime import datetime, timedelta

# Constants
NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/1.0"
DATA_DIR = "backend/data/raw"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S:%fZ"

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Function to fetch CVE data
def fetch_cve_data():
    # Calculate the date range for the past week
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    
    params = {
        "startIndex": 0,
        "resultsPerPage": 2000,  # Adjust this as needed
        "pubStartDate": start_date.strftime(DATE_FORMAT),
        "pubEndDate": end_date.strftime(DATE_FORMAT)
    }

    all_cve_data = []

    while True:
        response = requests.get(NVD_API_URL, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            break

        data = response.json()
        
        if 'result' not in data:
            print("Invalid response format")
            break

        all_cve_data.extend(data['result']['CVE_Items'])
        
        if len(data['result']['CVE_Items']) < params['resultsPerPage']:
            break  # No more data to fetch

        params['startIndex'] += params['resultsPerPage']

    # Save fetched data to a JSON file
    file_path = os.path.join(DATA_DIR, f"cve_data_{end_date.strftime('%Y%m%d')}.json")
    with open(file_path, 'w') as f:
        json.dump(all_cve_data, f, indent=4)

    print(f"Fetched {len(all_cve_data)} CVE entries. Data saved to {file_path}")

if __name__ == "__main__":
    fetch_cve_data()
