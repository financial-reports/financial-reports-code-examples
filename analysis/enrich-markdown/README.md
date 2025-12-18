# **Example: Enrich Markdown with AI (Gemini 2.5)**

This script demonstrates how to use **Google Gemini 2.5 Flash** to "beautify" or "enrich" the standard markdown files available from the FinancialReports API.

The standard API output is optimized for NLP and machine readability. This script post-processes that text to restore rich formatting—such as proper tables, hierarchical headings, and clean lists—making it suitable for human review or presentation.

## **Why Gemini 2.5 Flash?**

Unlike older methods that required splitting large documents into small chunks (which often broke table contexts or section continuity), **Gemini 2.5 Flash** features a context window large enough (1M+ tokens) to process entire Annual Reports (10-Ks) in a **single pass**.

This approach ensures:

* **Consistency:** Table column widths and formatting styles remain consistent across the whole document.  
* **Simplicity:** No complex threading or merging logic is required.  
* **Context:** The AI understands the full document structure, improving header hierarchy accuracy.

## **Setup**

1. **Create a virtual environment (recommended):**  
   python \-m venv venv  
   source venv/bin/activate  \# On Windows: venv\\Scripts\\activate

2. **Install the required Python packages:**  
   pip install \-r requirements.txt

## **Authentication**

This script is client-side and **does not** use your FR\_API\_KEY. It requires an API key from Google.

1. Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey).  
2. Set it as an environment variable before running the script:

**macOS / Linux:**

export GOOGLE\_API\_KEY="your\_api\_key\_here"

**Windows (PowerShell):**

$env:GOOGLE\_API\_KEY="your\_api\_key\_here"

## **Usage**

The script accepts two arguments:

* \--input-file: The path to the raw .md file (fetched from the FinancialReports API).  
* \--output-file: The path where you want to save the enriched markdown.

**Run command:**

python enrich\_markdown.py \\  
  \--input-file city\_of\_london\_raw.md \\  
  \--output-file city\_of\_london\_enriched.md

## **Expected Output**

You will see logs indicating the size of the file and the processing time. Note that processing a full 10-K may take 1-4 minutes depending on the complexity of the tables.

\--- Reading content from 'city\_of\_london\_raw.md' \---  
\--- Input Size: 745,916 characters \---  
\--- Sending to gemini-2.5-flash... (This may take 1-4 minutes for large filings) \---  
\--- Processing Complete in 210.4 seconds \---  
\--- Success\! Saved to 'city\_of\_london\_enriched.md' \---  

