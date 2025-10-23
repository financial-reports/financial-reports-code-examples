# Use Case: End-to-End Generative Sentiment Analysis

This example provides a Jupyter Notebook demonstrating a complete, end-to-end workflow for advanced financial analysis.

It is intended for **FinancialReports API Users** who want to:
1.  Programmatically find a specific filing (e.g., an annual report) using the FinancialReports API.
2.  Fetch the full Markdown content of that filing.
3.  Perform targeted, generative sentiment analysis on that content using the Google Gemini API.

This workflow shows how to combine our data with a large language model to get structured, actionable insights (Sentiment, Rationale, and Evidence) for any topic.

## How to Use

### 1. Set Up Your Environment

This script requires API keys for both FinancialReports and Google Gemini.

1.  Create a file named `.env` in this directory (`/use-cases/generative_sentiment_analysis_workflow/`).
2.  Add your keys to this file. Your `FR_API_KEY` is available from your FinancialReports dashboard.

    ```ini
    # .env
    FR_API_KEY="your_financial_reports_api_key_here"
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

### 2. Install Dependencies

Install the required Python libraries from this directory. It is highly recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook

Launch the Jupyter Notebook server:

```bash
jupyter notebook
```

Open `generative_sentiment_analysis.ipynb` in your browser and run the cells from top to bottom. The notebook is self-documenting and will guide you through each step of the process.