import os
import sys
import argparse
from typing import Callable, List, Dict, Any
from financial_reports_generated_client import ApiClient, Configuration
from financial_reports_generated_client.apis.tags import (
    isic_sections_api,
    isic_divisions_api,
    isic_groups_api,
    isic_classes_api,
)
from financial_reports_generated_client.exceptions import ApiException, UnauthorizedException

def get_api_key():
    """Fetches API key from environment and exits if not found."""
    api_key = os.environ.get("FR_API_KEY")
    if not api_key:
        print("Error: FR_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set it: export FR_API_KEY='your_api_key_here'", file=sys.stderr)
        sys.exit(1)
    return api_key

def get_api_config(api_key: str) -> Configuration:
    """Returns an API client configuration."""
    config = Configuration(api_key={'X-API-Key': api_key})
    config.host = "https://api.financialreports.eu"
    return config

def fetch_all_paginated(api_call: Callable, query_params: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    A helper function to fetch all results from a paginated endpoint.
    """
    all_results = []
    
    # Ensure page_size is set, default to 100
    query_params.setdefault('page_size', 100)
    
    try:
        # Make the initial API call
        response = api_call(query_params=query_params)
        all_results.extend(response.body.get('results', []))
        
        next_page_url = response.body.get('next')
        
        while next_page_url:
            print(f"  Fetching next page: {next_page_url}")
            
            try:
                page_query = next_page_url.split('?')[-1]
                params = dict(q.split('=') for q in page_query.split('&'))
                query_params['page'] = int(params['page'])
            except Exception:
                print(f"  Error parsing next page URL: {next_page_url}", file=sys.stderr)
                break # Stop pagination

            response = api_call(query_params=query_params)
            all_results.extend(response.body.get('results', []))
            next_page_url = response.body.get('next')
            
    except ApiException as e:
        print(f"\nError calling API: {e.body}", file=sys.stderr)
        sys.exit(1)
        
    return all_results

def list_sections(api_client: ApiClient):
    """Fetches and prints all ISIC Sections."""
    print("Fetching all ISIC Sections...")
    api_instance = isic_sections_api.IsicSectionsApi(api_client)
    
    sections = fetch_all_paginated(api_instance.isic_sections_list, {})
    
    print(f"Found {len(sections)} total Sections:")
    print("--------------------------------------------------")
    for section in sections:
        print(f"- [{section.get('code')}] {section.get('name')}")

def list_divisions_in_section(api_client: ApiClient, section_code: str):
    """Fetches and prints all Divisions for a given Section."""
    print(f"Fetching ISIC Divisions for Section '{section_code}'...")
    api_instance = isic_divisions_api.IsicDivisionsApi(api_client)
    
    # The filter parameter is 'sector'
    query_params = {'sector': section_code}
    divisions = fetch_all_paginated(api_instance.isic_divisions_list, query_params)
    
    print(f"Found {len(divisions)} total Divisions:")
    print("--------------------------------------------------")
    for division in divisions:
        print(f"- [{division.get('code')}] {division.get('name')}")

def list_groups_in_division(api_client: ApiClient, division_code: str):
    """Fetches and prints all Groups for a given Division."""
    print(f"Fetching ISIC Groups for Division '{division_code}'...")
    api_instance = isic_groups_api.IsicGroupsApi(api_client)
    
    # The filter parameter is 'industry_group'
    query_params = {'industry_group': division_code}
    groups = fetch_all_paginated(api_instance.isic_groups_list, query_params)
    
    print(f"Found {len(groups)} total Groups:")
    print("--------------------------------------------------")
    for group in groups:
        print(f"- [{group.get('code')}] {group.get('name')}")

def list_classes_in_group(api_client: ApiClient, group_code: str):
    """Fetches and prints all Classes for a given Group."""
    print(f"Fetching ISIC Classes for Group '{group_code}'...")
    api_instance = isic_classes_api.IsicClassesApi(api_client)
    
    # The filter parameter is 'industry'
    query_params = {'industry': group_code}
    classes = fetch_all_paginated(api_instance.isic_classes_list, query_params)
    
    print(f"Found {len(classes)} total Classes:")
    print("--------------------------------------------------")
    for iclass in classes:
        print(f"- [{iclass.get('code')}] {iclass.get('name')}")

def main():
    parser = argparse.ArgumentParser(
        description="Browse the ISIC classification hierarchy."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--list-sections', 
        action='store_true', 
        help="List all top-level ISIC Sections (Level 1)."
    )
    group.add_argument(
        '--list-divisions-in-section', 
        type=str,
        metavar='SECTION_CODE',
        help="List all Divisions (Level 2) in a specific Section (e.g., 'C')."
    )
    group.add_argument(
        '--list-groups-in-division', 
        type=str,
        metavar='DIVISION_CODE',
        help="List all Groups (Level 3) in a specific Division (e.g., '14')."
    )
    group.add_argument(
        '--list-classes-in-group', 
        type=str,
        metavar='GROUP_CODE',
        help="List all Classes (Level 4) in a specific Group (e.g., '141')."
    )
    
    args = parser.parse_args()
    
    api_key = get_api_key()
    config = get_api_config(api_key)

    try:
        with ApiClient(config) as api_client:
            if args.list_sections:
                list_sections(api_client)
            elif args.list_divisions_in_section:
                list_divisions_in_section(api_client, args.list_divisions_in_section)
            elif args.list_groups_in_division:
                list_groups_in_division(api_client, args.list_groups_in_division)
            elif args.list_classes_in_group:
                list_classes_in_group(api_client, args.list_classes_in_group)
                
    except UnauthorizedException:
        print("\nError: Authentication Failed. Check your API key.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()