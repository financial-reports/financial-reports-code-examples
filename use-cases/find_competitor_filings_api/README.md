# Use Case: Find Competitor Filings via API

## Purpose

This use case demonstrates how to solve a real-world financial analysis problem by intelligently chaining multiple calls to the FinancialReports API. It shows a user how to go beyond simple, single-endpoint queries to build a more powerful and insightful script.

The workflow performs the following steps:
1.  Identifies a company by its ISIN.
2.  Discovers the company's specific industry (ISIC code).
3.  Finds competitor companies in the same industry.
4.  Fetches the latest annual report for each of those competitors.

## Prerequisites

1.  **API Key:** You **must** have a valid FinancialReports API key.
2.  **Environment Variable:** You must set the `FR_API_KEY` environment variable. See the main `README.md` in the repository root for instructions.

## How to Run

1.  **Install Dependencies:**
    This notebook requires the official Python SDK and `pandas`.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch Jupyter:**
    Navigate to this directory in your terminal and start Jupyter Notebook or JupyterLab.
    ```bash
    jupyter notebook
    ```

3.  **Open and Run the Notebook:**
    Open the `find_competitor_filings.ipynb` file and run the cells sequentially. You can easily change the `target_isin` in the final cell to analyze the competitors of a different company.

## Files

* `find_competitor_filings.ipynb`: The main Jupyter Notebook containing the end-to-end API workflow.
* `README.md`: This file.
* `requirements.txt`: Lists the necessary Python packages.