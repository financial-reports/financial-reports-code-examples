import os
import sys
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import filing_types_api
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException

def list_all_filing_types():
    """
    Connects to the FinancialReports API and retrieves a complete,
    paginated list of all available filing types.
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

    print("Fetching all filing types (handling pagination)...")

    all_filing_types = []

    # 3. Use the ApiClient context manager
    with ApiClient(config) as api_client:
        # Instantiate the API
        api_instance = filing_types_api.FilingTypesApi(api_client)

        try:
            # 4. Make the initial API call
            # OperationId: 'filing_types_list'
            response = api_instance.filing_types_list(
                query_params={'page_size': 100} # Fetch 100 per page
            )
            
            # Add the first page of results
            all_filing_types.extend(response.body.get('results', []))
            
            # 5. Handle pagination
            # The SDK's response body contains the 'next' URL
            next_page_url = response.body.get('next')
            
            while next_page_url:
                print(f"Fetching next page: {next_page_url}")
                
                # The SDK client can't directly consume the 'next' URL.
                # We need to parse the 'page' number from it.
                try:
                    page_query = next_page_url.split('?')[-1]
                    params = dict(q.split('=') for q in page_query.split('&'))
                    next_page = int(params['page'])
                except Exception:
                    print(f"Error parsing next page URL: {next_page_url}", file=sys.stderr)
                    break # Stop pagination

                # Make the next API call with the new page number
                response = api_instance.filing_types_list(
                    query_params={'page_size': 100, 'page': next_page}
                )
                
                all_filing_types.extend(response.body.get('results', []))
                next_page_url = response.body.get('next')

            # 6. Print the complete list
            total_count = len(all_filing_types)
            
            # Note: response.body['count'] would be from the *last* page.
            # We use len(all_filing_types) for the true total fetched.
            print(f"Found {total_count} total filing types:")
            print("--------------------------------------------------")

            for filing_type in all_filing_types:
                code = filing_type.get('code', 'N/A')
                name = filing_type.get('name', 'N/A')
                desc = filing_type.get('description', 'No description.')
                print(f"- [{code}] {name}")
                print(f"  {desc}")


        except UnauthorizedException:
            print("\nError: Authentication Failed. Check your API key.", file=sys.stderr)
            sys.exit(1)
        except ApiException as e:
            print(f"\nError calling API: {e.body}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    list_all_filing_types()