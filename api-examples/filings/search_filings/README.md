# Example: Search Filings by Company and Date

This script demonstrates how to use the `GET /filings/` endpoint to perform an advanced search.

It finds all filings for a specific company (using `company_isin`) published after a specific date (using `release_datetime_from`). This script accepts command-line arguments to make it more flexible.

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

The script takes two arguments:
1.  `--isin`: The ISin of the company to search for (e.g., `DE000A1EWWW0` for adidas AG).
2.  `--start-date`: The date to search from, in `YYYY-MM-DD` format (e.g., `2024-01-01`).

**Example Command:**

```bash
python search_filings.py --isin DE000A1EWWW0 --start-date 2024-01-01
```

## Expected Output

You will see a list of filings matching your search criteria (details will vary):

Searching for filings with ISIN DE000A1EWWW0 released after 2024-01-01...
Found 3 matching filings:
-------------------------
- [2024-04-30] Filing ID 974971: Annual financial report 2023 (PDF)
- [2024-07-15] Filing ID 978123: Q2 Report 2024
- [2024-10-15] Filing ID 981456: Q3 Report 2024