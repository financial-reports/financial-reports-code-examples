# Example: List All Filing Types

This script demonstrates how to fetch a complete, paginated list of all available filing types from the `GET /filing-types/` endpoint.

This is a common "helper" script used to understand what `type` codes are available for filtering on the `/filings/` endpoint. The script will automatically handle pagination to retrieve all results.

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
```

## Run

```bash
python list_filing_types.py
```

## Expected Output

The script will print a complete list of all filing types and their codes (the list will be much longer in practice):

```
Fetching all filing types (handling pagination)...
Found 123 total filing types:
--------------------------------------------------
- [10-K] Annual Report
  Official yearly report covering company activity and full financial performance.
- [10-Q] Quarterly Report
  Official quarterly report covering company activity and financial performance.
- [8-K] Current Report
  Report of unscheduled material events or corporate changes.
- [20-F] Foreign Private Issuer Annual Report
  Annual report filed by certain foreign issuers.
... (and so on)
```