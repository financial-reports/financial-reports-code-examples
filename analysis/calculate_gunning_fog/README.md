# Analysis: Calculate Gunning Fog Readability Index

## Purpose

This example demonstrates how to calculate the **Gunning Fog Index**, a measure of text readability. It estimates the years of formal education needed to understand a text on the first reading.

This is a valuable tool for analyzing the complexity and transparency of financial filings.

## How to Run

1.  **Install Dependencies:**
    This notebook requires the `nltk` library.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch Jupyter:**
    Navigate to this directory in your terminal and start Jupyter Notebook or JupyterLab.
    ```bash
    jupyter notebook
    ```

3.  **Open and Run the Notebook:**
    Open the `calculate_gunning_fog.ipynb` file and run the cells sequentially. The notebook includes explanations for each step, from loading data to interpreting the final score.

## Files

* `calculate_gunning_fog.ipynb`: The main Jupyter Notebook with the analysis and explanations.
* `utils.py`: A Python module containing the reusable `calculate_gunning_fog` function.
* `sample_text.txt`: A sample paragraph from a fictional report to run the analysis on.
* `requirements.txt`: Lists the necessary Python packages.