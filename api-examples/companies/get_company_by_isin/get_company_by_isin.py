import os
import sys
import argparse
import json
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import companies_api
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException

def get_company_by_isin(isin: str):
    """
    Connects to the FinancialReports API and retrieves the full details
    for a company by its ISIN.
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

    print(f"Searching for company with ISIN {isin}...")

    # 3. Use the ApiClient context manager
    with ApiClient(config) as api_client:
        # Instantiate the Companies API
        api_instance = companies_api.CompaniesApi(api_client)

        try:
            # 4. Make the API call
            # OperationId: 'companies_list'
            # We filter by 'isin' and use 'view=full' to get all details
            response = api_instance.companies_list(
                query_params={
                    'isin': isin,
                    'view': 'full'
                }
            )

            results = response.body.get('results', [])
            count = response.body.get('count', 0)

            if count == 0:
                print(f"No company found with ISIN {isin}.")
                sys.exit(0)
            
            if count > 1:
                print(f"Warning: Found {count} companies matching ISIN {isin}. Displaying first result.")

            # 5. Process and print the full company object
            company = results[0]
            
            print(f"Successfully found company: {company.get('name')} (ID: {company.get('id')})")
            print("--------------------------------------------------")
            print(f"Name:         {company.get('name')}")
            print(f"Tagline:      {company.get('tagline')}")
            print(f"LEI:          {company.get('lei')}")
            print(f"Country:      {company.get('country_code')}")
            
            # Safely get nested sub_industry details
            sub_industry_name = "N/A"
            if company.get('sub_industry'):
                code = company['sub_industry'].get('code', '')
                name = company['sub_industry'].get('name', 'N/A')
                sub_industry_name = f"{code} - {name}"
                
            print(f"Industry:     {sub_industry_name}")
            print(f"Homepage:     {company.get('homepage_link')}")
            print(f"IR Page:      {company.get('ir_link')}")

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
    parser = argparse.ArgumentParser(
        description="Fetch full company details by ISIN."
    )
    parser.add_argument(
        "--isin",
        type=str,
        required=True,
        help="The company ISIN to look up (e.g., DE000A1EWWW0)."
    )
    
    args = parser.parse_args()
    get_company_by_isin(args.isin.strip())