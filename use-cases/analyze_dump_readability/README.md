# Use Case: Bulk Readability Analysis of Data Dump Filings

## Purpose

This use case is a complete workflow that demonstrates the power of combining different tools in the FinancialReports cookbook. It shows how to go from the raw metadata dump to a valuable analytical insight: the readability of hundreds or thousands of filings.

This notebook answers the question: **"Now that I've loaded my data into a database, what's a real-world analysis I can perform?"**

## Prerequisites

1.  **Database:** You **must** have already run the `load_metadata_csv_to_sqlite.py` script from the `/data-dump-processing` directory. This notebook requires the output of that script (the `financialreports.db` file).
2.  **Analysis Script:** This notebook depends on the `utils.py` file located in `/analysis/calculate_gunning_fog/`.
3.  **Data Dump Files:** To run this on your own data, you will need to download and unzip the actual markdown filings from a FinancialReports data dump. You must update the `DATA_DUMP_MARKDOWN_PATH` variable in the notebook to point to the location of these files.

## How to Run

1.  **Install Dependencies:**
    This notebook has several dependencies for data processing, database access, and plotting.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Launch Jupyter:**
    Navigate to this directory in your terminal and start Jupyter Notebook or JupyterLab.
    ```bash
    jupyter notebook
    ```

3.  **Open and Run the Notebook:**
    Open the `analyze_readability.ipynb` file and run the cells sequentially.

## Files

* `analyze_readability.ipynb`: The main Jupyter Notebook containing the end-to-end workflow.
* `README.md`: This file.
* `requirements.txt`: Lists the necessary Python packages.