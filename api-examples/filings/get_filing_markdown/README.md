# Example: Get Filing Markdown Content

This script demonstrates how to retrieve the raw, processed Markdown content for a single filing using its ID.

It uses the `GET /filings/{id}/markdown/` endpoint and saves the resulting text to a local file.

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
1.  `--filing-id`: The ID of the filing to fetch (e.g., `974971`).
2.  `--output-file`: The name of the file to save the content to (e.g., `report.md`).

**Example Command:**

```bash
python get_filing_markdown.py --filing-id 974971 --output-file adidas_report_2023.md
```

## Expected Output

The script will print a success message and create a new file in your directory.

Fetching markdown for filing ID 974971...
Successfully saved markdown content to adidas_report_2023.md