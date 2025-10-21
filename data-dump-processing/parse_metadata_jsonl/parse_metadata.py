import sys
import argparse
import pandas as pd

def parse_metadata(metadata_file: str, isin: str = None, filing_type: str = None):
    """
    Loads a .jsonl metadata file into pandas and filters it based on
    ISIN or filing_type.
    """
    
    print(f"Loading metadata from '{metadata_file}'...")
    
    try:
        # Load the JSON Lines file into a DataFrame
        # 'lines=True' tells pandas to read one JSON object per line
        df = pd.read_json(metadata_file, lines=True)
    except FileNotFoundError:
        print(f"Error: Metadata file not found: '{metadata_file}'", file=sys.stderr)
        print("Please ensure 'sample_metadata.jsonl' is in the same directory.", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print(f"Error: Failed to parse '{metadata_file}'. Is it a valid .jsonl file?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        print("Metadata file is empty. No documents to process.")
        return

    filtered_df = pd.DataFrame()

    if isin:
        # Filter by company_isin
        filtered_df = df[df['company_isin'].str.upper() == isin.upper()]
        print(f"Found {len(filtered_df)} documents for ISIN {isin}:")
        
    elif filing_type:
        # Filter by filing_type
        filtered_df = df[df['filing_type'].str.upper() == filing_type.upper()]
        print(f"Found {len(filtered_df)} documents for filing type '{filing_type}':")
        
    print("--------------------------------------------------")
    
    if filtered_df.empty:
        print("No matching documents found for your criteria.")
    else:
        # Print the resulting DataFrame to the console
        # 'to_string' provides a cleaner, aligned output
        print(filtered_df.to_string(index=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse and filter a .jsonl data dump metadata file."
    )
    
    # Add an argument for the metadata file, defaulting to the sample
    parser.add_argument(
        "-f", "--metadata-file",
        default="sample_metadata.jsonl",
        help="Path to the metadata .jsonl file (default: sample_metadata.jsonl)"
    )
    
    # Add mutually exclusive arguments for the filter criteria
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--isin",
        type=str,
        help="Filter documents by company ISIN (e.g., DE000A1EWWW0)."
    )
    group.add_argument(
        "--filing-type",
        type=str,
        help="Filter documents by filing type (e.g., 10-K)."
    )
    
    args = parser.parse_args()
    
    parse_metadata(args.metadata_file, args.isin, args.filing_type)