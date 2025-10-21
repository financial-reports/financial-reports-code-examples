# Example: Enrich Markdown with AI

This script demonstrates how to use a Large Language Model (LLM) to "enrich" or "beautify" the standard, NLP-optimized Markdown file available from the FinancialReports API.

The standard API output is designed for machine readability. This script post-processes that text to add back rich formatting, such as tables, headings, and lists, making it suitable for human review or presentation.

## Setup

1.  Create a virtual environment (recommended).
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Authentication

This script is client-side and **does not** use your `FR_API_KEY`. It requires an API key from an LLM provider (e.g., Google, OpenAI).

Set the appropriate key as an environment variable *before* running the script.

**For Google Gemini (Default):**

Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey) and set it:
```bash
# On macOS / Linux
export GOOGLE_API_KEY="your_api_key_here"
```

**For OpenAI:**

```bash
# On macOS / Linux
export OPENAI_API_KEY="your_api_key_here"
```

**For Anthropic:**

```bash
# On macOS / Linux
export ANTHROPIC_API_KEY="your_api_key_here"
```

## Run

The script takes two required arguments:
1.  `--input-file`: The path to the standard `report.md` file you've fetched from our API.
2.  `--output-file`: The path to save the new, enriched file.

It also accepts an optional `--model` argument to choose the provider.

**Example using Google Gemini (Default):**

```bash
python enrich_markdown.py \
  --input-file city_of_london_standard.md \
  --output-file city_of_london_enriched.md
```

**Example using OpenAI:**

```bash
python enrich_markdown.py \
  --model openai \
  --input-file city_of_london_standard.md \
  --output-file city_of_london_enriched_openai.md
```

## Expected Output

The script will process the file in parallel chunks and save the result.

```
Using gemini provider...
--- 1. Reading content from 'city_of_london_standard.md' ---
--- 2. Document split into 116 physical chunks ---
--- 3. Processing all 116 chunks in parallel... ---
--- Processing chunk 1... ---
--- Processing chunk 2... ---
--- Processing chunk 5... ---
...
--- Processing chunk 115... ---
--- Processing chunk 116... ---
--- 4. All chunks processed. Merging... ---
--- 5. Successfully saved enriched output to 'city_of_london_enriched.md' ---

--- 6. Process Complete ---
```