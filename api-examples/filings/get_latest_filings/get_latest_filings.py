import os
import sys
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import filings_api
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException

def get_latest_filings():
    """
    Connects to the FinancialReports API and fetches the 5 most recent filings.
    """
    
    # 1. Get API Key from environment variable (as per our contribution guidelines)
    api_key = os.environ.get("FR_API_KEY")
    if not api_key:
        print("Error: FR_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set it: export FR_API_KEY='your_api_key_here'", file=sys.stderr)
        sys.exit(1)

    # 2. Configure the API client
    # The SDK is generated to look for the 'X-API-Key' header.
    config = Configuration(
        api_key={'X-API-Key': api_key}
    )
    
    # Set the host URL from the OpenAPI spec
    config.host = "https://api.financialreports.eu"

    print("Connecting to API to fetch latest filings...")

    # 3. Use the ApiClient context manager for proper resource management
    with ApiClient(config) as api_client:
        
        # Instantiate the specific API we want to use
        # (based on the 'tags' in the OpenAPI spec)
        api_instance = filings_api.FilingsApi(api_client)

        try:
            # 4. Make the API call
            # OperationId: 'filings_list'
            # We sort by 'release_datetime' in descending order and limit to 5 results
            response = api_instance.filings_list(
                ordering="-release_datetime",
                page_size=5,
            )

            results = response.body.get('results', [])
            print(f"Found {len(results)} recent filings:")
            print("-------------------------")

            # 5. Process and print results
            # We parse the 'FilingSummary' schema
            for filing in results:
                date = filing.get('release_datetime', 'N/A').split('T')[0]
                title = filing.get('title', 'No Title')
                filing_id = filing.get('id', 'N/A')
                print(f"- [{date}] Filing ID {filing_id}: {title}")

        except UnauthorizedException:
            print("\nError: Authentication Failed. Your API Key is invalid or missing.", file=sys.stderr)
            sys.exit(1)
        except ApiException as e:
            print(f"\nError calling API: {e.body}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    get_latest_filings()