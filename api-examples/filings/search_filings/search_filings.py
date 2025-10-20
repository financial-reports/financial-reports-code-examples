import os
import sys
import argparse
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import filings_api
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException

def search_filings(isin: str, start_date: str):
    """
    Connects to the FinancialReports API and searches for filings based on
    a company ISIN and a release start date.
    """
    
    # 1. Get API Key from environment variable
    api_key = os.environ.get("FR_API_KEY")
    if not api_key:
        print("Error: FR_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set it: export FR_API_KEY='your_api_key_here'", file=sys.stderr)
        sys.exit(1)

    # 2. Configure the API client
    config = Configuration(
        api_key={'X-API-Key': api_key}
    )
    config.host = "https://api.financialreports.eu"

    print(f"Searching for filings with ISIN {isin} released after {start_date}...")

    # 3. Use the ApiClient context manager
    with ApiClient(config) as api_client:
        api_instance = filings_api.FilingsApi(api_client)

        try:
            # 4. Make the API call using filter parameters
            # OperationId: 'filings_list'
            # We filter by 'company_isin' and 'release_datetime_from'
            # The API spec expects 'release_datetime_from' as a full datetime,
            # so we append T00:00:00Z to the user's YYYY-MM-DD input.
            start_datetime = f"{start_date}T00:00:00Z"

            response = api_instance.filings_list(
                company_isin=isin,
                release_datetime_from=start_datetime,
                ordering="-release_datetime", # Sort newest first
            )

            results = response.body.get('results', [])
            count = response.body.get('count', 0)

            print(f"Found {count} matching filings:")
            print("-------------------------")

            if not results:
                print("No results found for this query.")
                return

            # 5. Process and print results
            for filing in results:
                date = filing.get('release_datetime', 'N/A').split('T')[0]
                title = filing.get('title', 'No Title')
                filing_id = filing.get('id', 'N/A')
                print(f"- [{date}] Filing ID {filing_id}: {title}")

        except UnauthorizedException:
            print("\nError: Authentication Failed. Check your API key.", file=sys.stderr)
            sys.exit(1)
        except ApiException as e:
            # Check for 400 Bad Request, e.g., invalid date format
            if e.status == 400:
                print(f"\nError: Bad Request. Check your parameters.", file=sys.stderr)
                print(f"Details: {e.body}", file=sys.stderr)
            else:
                print(f"\nError calling API: {e.body}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    # Use argparse to accept command-line arguments
    parser = argparse.ArgumentParser(
        description="Search FinancialReports filings by ISIN and start date."
    )
    parser.add_argument(
        "--isin",
        required=True,
        help="Company ISIN to search for (e.g., DE000A1EWWW0)"
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Start date in YYYY-MM-DD format (e.g., 2024-01-01)"
    )
    
    args = parser.parse_args()
    
    # Basic validation for date format (simple check)
    if len(args.start_date) != 10 or args.start_date[4] != '-' or args.start_date[7] != '-':
        print(f"Error: Invalid date format: '{args.start_date}'.", file=sys.stderr)
        print("Please use YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)

    search_filings(args.isin, args.start_date)