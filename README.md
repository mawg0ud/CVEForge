# CVE Database and Analysis

This repository tracks the latest Common Vulnerabilities and Exposures (CVE). It includes:
- A script to scrape CVE databases for the latest vulnerabilities.
- Analysis of significant CVEs, explaining their impact and mitigation.
- Scripts for automating the notification of new CVEs related to specific software.

## Features

- **Fetch Latest CVEs**: Fetches the latest CVEs from the NVD API.
- **Analyze CVEs**: Analyzes fetched CVEs to determine significance based on CVSS scores.
- **Notify Users**: Notifies users via email about significant CVEs related to their subscribed software.
- **API Endpoints**: Provides a RESTful API to interact with the CVE database and user preferences.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/mawg0ud/CVEForge.git
    cd cve-database-analysis
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Environment Variables**:
    - Create a `.env` file in the root directory and add the following configuration settings:
    ```env
    NVD_API_URL=https://services.nvd.nist.gov/rest/json/cves/1.0
    RESULTS_PER_PAGE=2000
    DATE_FORMAT=%Y-%m-%dT%H:%M:%S:%fZ

    RAW_DATA_DIR=backend/data/raw
    PROCESSED_DATA_DIR=backend/data/processed
    SIGNIFICANT_CVE_FILE=significant_cve.json

    USER_DB=backend/data/users.db

    SMTP_SERVER=smtp.example.com
    SMTP_PORT=587
    SMTP_USERNAME=your_email@example.com
    SMTP_PASSWORD=your_email_password
    EMAIL_SENDER=your_email@example.com

    LOG_FILE=backend/logs/app.log
    LOG_LEVEL=INFO
    ```

6. **Initialize the User Database**:
    - Create the SQLite database and table for user preferences:
    ```bash
    sqlite3 backend/data/users.db "CREATE TABLE user_preferences (email TEXT, software TEXT);"
    ```

## Usage

1. **Run the Application**:
    ```bash
    python app.py
    ```

2. **API Endpoints**:
    - **Fetch CVE Data**: `GET /fetch`
    - **Analyze CVE Data**: `GET /analyze`
    - **Notify Users**: `GET /notify`
    - **Get Significant CVEs**: `GET /significant-cves`
    - **Add User Preference**: `POST /add-user`
        - JSON Body: `{"email": "user@example.com", "software": "software1"}`

    You can test the API endpoints using tools like `curl` or Postman.

## Example Requests

- **Fetch CVE Data**:
    ```bash
    curl -X GET http://127.0.0.1:5000/fetch
    ```

- **Analyze CVE Data**:
    ```bash
    curl -X GET http://127.0.0.1:5000/analyze
    ```

- **Notify Users**:
    ```bash
    curl -X GET http://127.0.0.1:5000/notify
    ```

- **Get Significant CVEs**:
    ```bash
    curl -X GET http://127.0.0.1:5000/significant-cves
    ```

- **Add User Preference**:
    ```bash
    curl -X POST http://127.0.0.1:5000/add-user -H "Content-Type: application/json" -d '{"email": "user@example.com", "software": "software1"}'
    ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you wish to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
