# Example: Get Company Details by ISIN

This script demonstrates how to look up a company using its ISIN.

It uses the `GET /companies/` endpoint with the `isin` filter and the `view=full` parameter to retrieve all available details for the matching company.

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