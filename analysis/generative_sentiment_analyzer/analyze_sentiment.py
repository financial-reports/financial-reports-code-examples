"""
FinancialReports Analysis Script: Generative Sentiment Analyzer

This script analyzes a local text/markdown file for sentiment regarding a
specific user-provided question. It uses the Google Gemini API to provide a
structured JSON response.

Usage:
    python analyze_sentiment.py \
        --file "path/to/your/document.md" \
        --question "What is the sentiment regarding future outlook?"

Security:
    Requires the 'GEMINI_API_KEY' environment variable to be set.
"""

import os
import sys
import argparse
import json
import google.generai as genai
from google.generai import types
from dotenv import load_dotenv

def get_gemini_client():
    """
    Initializes and returns the Gemini client, checking for the API key.
    """
    load_dotenv()  # Load .env file if it exists
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please set the variable or create a '.env' file with its value.")
        sys.exit(1)
        
    try:
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        sys.exit(1)

def get_analysis_schema():
    """
    Returns the structured JSON schema for the generative model.
    """
    return types.Schema(
        type=types.Type.OBJECT,
        required=["sentiment_category", "rationale"],
        properties={
            "sentiment_category": types.Schema(
                type=types.Type.STRING,
                description="The single most appropriate sentiment category.",
                enum=[
                    "Very Positive",
                    "Positive",
                    "Neutral",
                    "Negative",
                    "Very Negative",
                ],
            ),
            "rationale": types.Schema(
                type=types.Type.STRING,
                description="A brief, 1-2 sentence justification for the chosen "
                            "sentiment, explaining *why* it was selected."
            ),
            "supporting_evidence": types.Schema(
                type=types.Type.ARRAY,
                description="A list of 1-3 direct quotes from the text that "
                            "support the rationale.",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
    )

def build_prompt(content, question):
    """
    Creates the final prompt text to be sent to the model.
    """
    return f"""
    You are a professional financial analyst. Your task is to analyze the
    following financial document excerpt based *only* on the text provided.
    
    You must answer a specific question and provide your response *only*
    in the requested JSON format. Do not add any other text before or after
    the JSON object.

    **Analysis Question:**
    {question}

    **Document Content:**
    ---
    {content}
    ---
    """

def analyze_document_sentiment(client, content, question):
    """
    Sends the content and question to the Gemini API for analysis.
    """
    model = "gemini-flash-latest"
    schema = get_analysis_schema()
    prompt = build_prompt(content, question)

    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=schema,
    )

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    print("Analyzing document... (This may take a moment)")
    try:
        # Use the non-streaming generate_content for a single JSON response
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )
        return response.text
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

def main():
    """
    Main execution function: parses arguments, reads file, triggers analysis.
    """
    parser = argparse.ArgumentParser(
        description="Analyze sentiment of a local financial document.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the .md or .txt file to analyze."
    )
    parser.add_argument(
        "--question",
        required=True,
        help="The specific question to ask about the document.\n"
             "Example: \"What is the sentiment regarding 'Business Outlook'?\""
    )
    args = parser.parse_args()

    # Read file content
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {args.file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    if not content.strip():
        print(f"Error: File '{args.file}' is empty.")
        sys.exit(1)

    client = get_gemini_client()
    result_json_text = analyze_document_sentiment(
        client, 
        content, 
        args.question
    )

    if result_json_text:
        print("\n--- Analysis Result ---")
        try:
            # Format the JSON for clean printing
            parsed_json = json.loads(result_json_text)
            print(json.dumps(parsed_json, indent=2))
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON response from API.")
            print(f"Raw response: {result_json_text}")
        print("-----------------------")

if __name__ == "__main__":
    main()
