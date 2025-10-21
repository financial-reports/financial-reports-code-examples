import argparse
import logging
import sqlite3
import sys
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from tqdm import tqdm

# Configure logging for clear output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# --- Configuration ---
# Use a chunk size to handle very large CSV files without consuming too much memory.
CHUNK_SIZE = 10000
# The name of the table to be created in the SQLite database.
TABLE_NAME = "filings_metadata"


def create_sqlite_engine(db_path: Path):
    """Creates a SQLAlchemy engine for the specified SQLite database file."""
    try:
        # The /// syntax is for a relative path from the current directory.
        engine = create_engine(f"sqlite:///{db_path}")
        return engine
    except SQLAlchemyError as e:
        logging.error(f"Failed to create database engine: {e}")
        sys.exit(1)


def validate_input_file(file_path: Path):
    """Validates that the input file exists and is a .csv file."""
    if not file_path.exists():
        logging.error(f"Input file not found: {file_path}")
        sys.exit(1)
    if file_path.suffix.lower() != ".csv":
        logging.warning(
            f"Input file '{file_path}' is not a .csv file. "
            "Attempting to process anyway."
        )


def load_csv_to_sqlite(
    csv_path: Path, engine, table_name: str, chunk_size: int
) -> int:
    """
    Loads data from a CSV file into a SQLite database table in chunks.

    Args:
        csv_path: Path to the input CSV file.
        engine: The SQLAlchemy engine instance.
        table_name: The name of the database table.
        chunk_size: The number of rows to process per chunk.

    Returns:
        The total number of rows processed.
    """
    total_rows = 0
    start_time = time.time()
    header = True
    if_exists_action = "replace"  # The first chunk replaces the table if it exists.

    logging.info(f"Starting to process '{csv_path}'...")
    logging.info(f"Target table: '{table_name}' in '{engine.url.database}'.")

    try:
        # Use tqdm to create a progress bar by iterating over the CSV in chunks.
        with pd.read_csv(
            csv_path, chunksize=chunk_size, iterator=True
        ) as reader:
            # Get total number of rows for tqdm progress bar if possible
            # This might be slow for very large files, but provides great UX.
            try:
                row_count = sum(1 for row in open(csv_path, 'r')) -1 # -1 for header
                pbar = tqdm(total=row_count, unit="rows", ncols=80)
            except Exception:
                pbar = tqdm(unit="rows", ncols=80)


            for chunk in reader:
                chunk.to_sql(
                    table_name,
                    engine,
                    if_exists=if_exists_action,
                    index=False,
                )
                # After the first chunk, append to the now-existing table.
                if_exists_action = "append"
                total_rows += len(chunk)
                pbar.update(len(chunk))
            
            pbar.close()

    except FileNotFoundError:
        logging.error(f"Error: The file '{csv_path}' was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logging.error(f"Error: The file '{csv_path}' is empty.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

    end_time = time.time()
    duration = end_time - start_time

    logging.info(
        f"Successfully processed {total_rows:,} rows in {duration:.2f} seconds."
    )
    return total_rows


def main():
    """Main function to parse arguments and run the ETL process."""
    parser = argparse.ArgumentParser(
        description="Load FinancialReports metadata from a CSV file into a SQLite database.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to the input metadata CSV file.",
    )
    parser.add_argument(
        "--db-name",
        type=Path,
        default="financialreports.db",
        help="Name of the SQLite database file to create.",
    )
    parser.add_argument(
        "--table-name",
        type=str,
        default=TABLE_NAME,
        help="Name of the table to store metadata in.",
    )
    args = parser.parse_args()

    validate_input_file(args.input)
    engine = create_sqlite_engine(args.db_name)

    load_csv_to_sqlite(args.input, engine, args.table_name, CHUNK_SIZE)

    logging.info("Process complete.")
    logging.info(f"You can now query your data in '{args.db_name}'.")
    logging.info(f"Example query tool: `sqlite3 {args.db_name}`")


if __name__ == "__main__":
    main()