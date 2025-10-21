# Analysis: Count Keyword Mentions

## Purpose

This example demonstrates how to count the occurrences of a predefined list of keywords within a text file. This is a foundational technique for thematic analysis, trend tracking (e.g., mentions of "AI" or "ESG" over time), and risk assessment.

The results are presented in a clean `pandas` DataFrame, a standard format for data analysis.

## How to Run

1.  **Install Dependencies:**
    This notebook requires the `pandas` library.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch Jupyter:**
    Navigate to this directory in your terminal and start Jupyter Notebook or JupyterLab.
    ```bash
    jupyter notebook
    ```

3.  **Open and Run the Notebook:**
    Open the `count_keywords.ipynb` file and run the cells sequentially. You can easily modify the `keywords_to_track` list in the second code cell to search for your own terms.

## Files

* `count_keywords.ipynb`: The main Jupyter Notebook with the analysis and explanations.
* `filing_snippet.txt`: A sample paragraph from a fictional report to run the analysis on.
* `requirements.txt`: Lists the necessary Python packages.