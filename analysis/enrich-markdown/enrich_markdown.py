import os
import sys
import argparse
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# --- Configuration ---
# We use Gemini 2.5 Flash for its balance of speed, cost, and massive context window.
MODEL_ID = "gemini-2.5-flash"

def main():
    # 1. Load Environment Variables
    load_dotenv()
    
    # 2. Parse Arguments
    parser = argparse.ArgumentParser(
        description="Enrich FinancialReports markdown using Gemini 2.5 Flash."
    )
    parser.add_argument("--input-file", required=True, help="Path to the standard .md file.")
    parser.add_argument("--output-file", required=True, help="Path to save the enriched .md file.")
    
    args = parser.parse_args()

    # 3. Validation
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.", file=sys.stderr)
        sys.exit(1)

    # 4. Read Content
    print(f"--- Reading content from '{args.input_file}' ---")
    with open(args.input_file, 'r', encoding='utf-8') as f:
        raw_markdown = f.read()

    print(f"--- Input Size: {len(raw_markdown):,} characters ---")

    # 5. Initialize Client
    client = genai.Client(api_key=api_key)

    # 6. Define Prompt
    system_instruction = """
    You are an expert financial document formatter. 
    Your task is to take the provided raw text (which is a 10-K filing converted from HTML/PDF) and format it into perfect, readable Markdown.
    
    Rules:
    1. Do NOT summarize. Do NOT omit any text. Keep the content exactly as is.
    2. Format financial tables using Markdown tables. Ensure headers align correctly.
    3. Use proper # H1, ## H2, ### H3 tags for headers based on the document structure.
    4. Fix broken line breaks inside paragraphs.
    5. Return ONLY the markdown.
    """

    config = types.GenerateContentConfig(
        temperature=0.1,
        system_instruction=system_instruction
    )

    # 7. Generate
    print(f"--- Sending to {MODEL_ID}... (This may take 1-4 minutes for large filings) ---")
    start_time = time.time()
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=raw_markdown,
            config=config
        )
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

    elapsed = time.time() - start_time
    print(f"--- Processing Complete in {elapsed:.1f} seconds ---")

    # 8. Save
    try:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"--- Success! Saved to '{args.output_file}' ---")
    except Exception as e:
        print(f"Error saving file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
