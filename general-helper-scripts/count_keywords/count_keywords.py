import sys
import argparse
import re
from collections import defaultdict

# --- Keyword Configuration ---
# Clients can easily modify this dictionary
ESG_KEYWORDS = {
    "Environmental": [
        "sustainability",
        "climate change",
        "ghg",
        "greenhouse gas",
        "emissions",
        "renewable",
        "carbon footprint"
    ],
    "Social": [
        "diversity",
        "inclusion",
        "human rights",
        "employee well-being",
        "social responsibility",
        "community"
    ],
    "Governance": [
        "board independence",
        "shareholder rights",
        "executive compensation",
        "corporate governance",
        "ethics"
    ]
}
# ------------------------------

def count_keywords_in_file(filepath: str, keyword_map: dict):
    """
    Reads a file and counts occurrences of keywords, grouped by category.
    
    Performs a case-insensitive search using word boundaries.
    """
    
    print(f"Analyzing '{filepath}' for ESG keywords...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read the entire file and convert to lowercase for searching
            text = f.read().lower()
            
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Use defaultdict to automatically initialize category counts
    category_counts = defaultdict(dict)
    total_mentions = 0
    
    for category, keywords in keyword_map.items():
        for keyword in keywords:
            # We must use re.escape to handle keywords that might have
            # special regex characters (e.g., "S&P").
            # \b ensures we match whole words only.
            pattern = rf'\b{re.escape(keyword.lower())}\b'
            
            try:
                matches = re.findall(pattern, text)
                count = len(matches)
                
                # Store the count using the original keyword casing
                category_counts[category][keyword] = count
                total_mentions += count
                
            except re.error as e:
                print(f"Warning: Could not process keyword '{keyword}': {e}", file=sys.stderr)

    # --- Print the results ---
    print(f"Found {total_mentions} total keyword mentions.")
    print("--------------------------------------------------")
    
    for category, keywords in category_counts.items():
        print(f"{category}:")
        if not any(keywords.values()):
            print("  (No mentions found)")
        
        for keyword, count in keywords.items():
            if count > 0:
                print(f"- {keyword}: {count}")
        print("") # Add a blank line for readability

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count occurrences of predefined ESG keywords in a text file."
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Path to the text or markdown file to analyze."
    )
    
    args = parser.parse_args()
    
    count_keywords_in_file(args.file, ESG_KEYWORDS)