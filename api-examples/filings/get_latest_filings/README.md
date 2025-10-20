# Example: Get Latest Filings

This script demonstrates how to use the FinancialReports Python SDK to connect to the API and fetch the 5 most recent filings.

It uses the `GET /filings/` endpoint, sorted by `release_datetime` in descending order.

## Setup

1.  Install the required Python package:
    ```bash
    pip install -r requirements.txt
    ```

## Authentication

This script requires your FinancialReports API key. Set it as an environment variable.

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_api_key_here"
```

## Run

```bash
python get_latest_filings.py
```

## Expected Output

You will see a printed list of the 5 most recent filing objects (details will vary based on live data):

Connecting to API to fetch latest filings...
Found 5 recent filings:
-------------------------
- [2025-10-20] Filing ID 98765: Annual Report 2024 - Demo Corp
- [2025-10-20] Filing ID 98764: Q3 Report 2025 - Sample Inc
- [2025-10-19] Filing ID 98763: Annual Report 2024 - Test AG
- [2025-10-19] Filing ID 98762: Half-Year Report 2025 - Demo PLC
- [2025-10-18] Filing ID 98761: Q1 Report 2025 - Beta Ltd