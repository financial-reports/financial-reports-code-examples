# Analysis Example: Generative Sentiment Analyzer

This example provides a command-line script to analyze the sentiment of a local text or markdown file regarding a specific topic.

It is intended for users who have local filing data, such as from a **FinancialReports Data Dump**, and want to perform advanced analysis.

The script uses the Google Gemini API with a strict JSON schema to return a 5-point sentiment score, a rationale, and supporting evidence.

## How to Use

### 1. Set Up Your Environment

This script requires a Google Gemini API key.

1.  Create a file named `.env` in this directory (`/analysis/generative_sentiment_analyzer/`).
2.  Add your API key to this file:

    ```ini
    # .env
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

### 2. Install Dependencies

Install the required Python libraries from this directory:

```bash
pip install -r requirements.txt
```

### 3. Run the Analysis

Run the `analyze_sentiment.py` script from your terminal, providing a file path and a question.

You can use the included `example_report.md` file to test:

```bash
python analyze_sentiment.py \
    --file "example_report.md" \
    --question "What is the sentiment regarding 'Business Outlook'?"

**Example Output:**

The script will contact the API and print a structured JSON response:

```json
{
  "sentiment_category": "Negative",
  "rationale": "The report highlights 'significant headwinds' and 'flat revenue growth' that 'did not meet initial targets.' While it mentions resilience and cautious optimism, the primary discussion of the 2024 outlook is dominated by challenges and missed goals.",
  "supporting_evidence": [
    "The fiscal year 2024 presented significant headwinds, including supply chain disruptions and inflationary pressures.",
    "company successfully maintained a flat revenue growth, which, while not meeting our initial targets, demonstrates operational resilience.",
    "regulatory uncertainty in the DACH region remains a considerable risk"
  ]
}