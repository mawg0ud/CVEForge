import os
import json
import pandas as pd

# Constants
RAW_DATA_DIR = "backend/data/raw"
PROCESSED_DATA_DIR = "backend/data/processed"
SIGNIFICANT_CVE_FILE = "significant_cve.json"

# Ensure processed data directory exists
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# Function to load raw CVE data from JSON files
def load_raw_data():
    cve_data = []
    for filename in os.listdir(RAW_DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(RAW_DATA_DIR, filename), 'r') as f:
                cve_data.extend(json.load(f))
    return cve_data

# Function to analyze CVE data and filter significant CVEs
def analyze_cve_data(cve_data):
    significant_cves = []

    for cve in cve_data:
        cve_id = cve['cve']['CVE_data_meta']['ID']
        description = cve['cve']['description']['description_data'][0]['value']
        cvss_v3 = cve['impact'].get('baseMetricV3', {})
        cvss_v2 = cve['impact'].get('baseMetricV2', {})

        # Extract CVSS scores and vectors
        cvss_v3_score = cvss_v3.get('cvssV3', {}).get('baseScore', 0)
        cvss_v2_score = cvss_v2.get('cvssV2', {}).get('baseScore', 0)

        # Determine if the CVE is significant (e.g., CVSS v3 score >= 7.0 or CVSS v2 score >= 7.0)
        if cvss_v3_score >= 7.0 or cvss_v2_score >= 7.0:
            significant_cves.append({
                "CVE_ID": cve_id,
                "Description": description,
                "CVSS_v3_Score": cvss_v3_score,
                "CVSS_v2_Score": cvss_v2_score
            })

    return significant_cves

# Function to save analyzed data
def save_analyzed_data(significant_cves):
    file_path = os.path.join(PROCESSED_DATA_DIR, SIGNIFICANT_CVE_FILE)
    with open(file_path, 'w') as f:
        json.dump(significant_cves, f, indent=4)

    print(f"Analyzed {len(significant_cves)} significant CVE entries. Data saved to {file_path}")

if __name__ == "__main__":
    raw_data = load_raw_data()
    significant_cve_data = analyze_cve_data(raw_data)
    save_analyzed_data(significant_cve_data)
