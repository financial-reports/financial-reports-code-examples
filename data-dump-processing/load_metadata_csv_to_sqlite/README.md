# Example: Load Data Dump Metadata CSV into a SQLite Database

## Purpose

FinancialReports data dumps often start with a large metadata CSV file containing information about millions of filings. Directly working with a massive CSV file can be slow and inefficient for complex queries.

This script solves that problem by loading the entire metadata CSV into a local, high-performance SQLite database. This transforms your flat file into a structured database, allowing you to run complex SQL queries instantly without needing to read the entire CSV each time.

**The primary benefit:** Go from a slow, multi-gigabyte CSV to a fast, indexed, and queryable database in minutes.

## Setup

1.  **Install Dependencies:**
    This script requires `pandas`, `sqlalchemy`, and `tqdm`. Install them using the provided requirements file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, pointing it to your metadata CSV file.

```bash
python load_to_sqlite.py --input /path/to/your/metadata.csv
```

### Command-Line Arguments

* `--input` (Required): The path to the source metadata CSV file.
* `--db-name` (Optional): The name of the SQLite database file to be created. Defaults to `financialreports.db`.
* `--table-name` (Optional): The name of the table to create within the database. Defaults to `filings_metadata`.

**Example with all arguments:**

```bash
python load_to_sqlite.py \
  --input "sample_metadata.csv" \
  --db-name "my_filings.db" \
  --table-name "filings"
```

### Expected Output

The script will display a progress bar as it processes the CSV file in chunks. Upon completion, you will see a success message.

```plaintext
2024-10-21 15:01:00,123 [INFO] Starting to process 'sample_metadata.csv'...
2024-10-21 15:01:00,124 [INFO] Target table: 'filings_metadata' in 'financialreports.db'.
100%|██████████| 15/15 [00:00<00:00, 5000 rows/s]
2024-10-21 15:01:00,200 [INFO] Successfully processed 15 rows in 0.08 seconds.
2024-10-21 15:01:00,201 [INFO] Process complete.
2024-10-21 15:01:00,202 [INFO] You can now query your data in 'financialreports.db'.
2024-10-21 15:01:00,203 [INFO] Example query tool: `sqlite3 financialreports.db`
```

## Next Steps

Once the data is loaded, you can connect to the `financialreports.db` file from any tool that supports SQLite, including:

* The `sqlite3` command-line tool.
* Python scripts (using `sqlite3` or `sqlalchemy`).
* Database clients like DBeaver or DB Browser for SQLite.
* Jupyter Notebooks, for interactive analysis (see `/use-cases/analyze_dump_readability/`).