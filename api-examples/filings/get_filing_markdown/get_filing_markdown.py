import os
import sys
import argparse
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import filings_api
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException, NotFoundException

def get_filing_markdown(filing_id: int, output_file: str):
    """
    Connects to the FinancialReports API and retrieves the raw markdown
    content for a specific filing, saving it to a file.
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

    print(f"Fetching markdown for filing ID {filing_id}...")

    # 3. Use the ApiClient context manager
    with ApiClient(config) as api_client:
        api_instance = filings_api.FilingsApi(api_client)

        try:
            # 4. Make the API call
            # OperationId is 'filings_markdown_retrieve'
            # This endpoint returns raw text, not JSON.
            response = api_instance.filings_markdown_retrieve(
                path_params={'id': filing_id}
            )

            # The raw text content is in response.body
            markdown_content = response.body
            
            # 5. Write the content to the specified output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            print(f"Successfully saved markdown content to {output_file}")

        except UnauthorizedException:
            print("\nError: Authentication Failed. Check your API key.", file=sys.stderr)
            sys.exit(1)
        except NotFoundException:
            print(f"\nError: Filing not found. No filing with ID {filing_id} exists.", file=sys.stderr)
            sys.exit(1)
        except ApiException as e:
            print(f"\nError calling API: {e.body}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch a filing's raw markdown content."
    )
    parser.add_argument(
        "--filing-id",
        type=int,
        required=True,
        help="The unique ID of the filing."
    )
    parser.add_argument(
        "--output-file",
        type=str,
        required=True,
        help="The local filename to save the markdown to (e.g., report.md)"
    )
    
    args = parser.parse_args()
    get_filing_markdown(args.filing_id, args.output_file)