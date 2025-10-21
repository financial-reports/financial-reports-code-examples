
# Example: List All Countries

This script fetches a complete, paginated list of all supported countries from the `GET /countries/` endpoint.

This is a common "helper" script to see which `alpha_2` codes can be used for filtering on the `/companies/` and `/filings/` endpoints. The script automatically handles pagination to retrieve all results.

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
python list_countries.py
```

## Expected Output

The script will print a complete list of all supported countries and their ISO codes (the list will be much longer in practice):

```
Fetching all countries (handling pagination)...
Found 249 total countries:
--------------------------------------------------
- [AF] Afghanistan (AFG)
- [AX] Åland Islands (ALA)
- [AL] Albania (ALB)
- [DZ] Algeria (DZA)
- [AS] American Samoa (ASM)
- [DE] Germany (DEU)
... (and so on)
```