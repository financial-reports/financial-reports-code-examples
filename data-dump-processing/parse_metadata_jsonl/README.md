# Example: Parse Data Dump Metadata

This script demonstrates a common data dump processing task: parsing the `metadata.jsonl` file to find specific documents.

It uses the `pandas` library to load the metadata into a DataFrame and then filters it based on user-provided criteria (e.g., by company ISIN or filing type).

## Setup

1.  Install the required Python package:
    ```bash
    pip install -r requirements.txt
    ```

## Run

The script can filter by ISIN or filing type.

**1. Find all documents for a specific company (by ISIN):**

```bash
python parse_metadata.py --isin DE000A1EWWW0
```

**Expected Output:**

```
Loading metadata from 'sample_metadata.jsonl'...
Found 3 documents for ISIN DE000A1EWWW0:
--------------------------------------------------
   filing_id company_name company_isin filing_type release_date                local_file_path
0     974971    adidas AG  DE000A1EWWW0        10-K   2024-04-30   filings/DE/adidas/974971.md
1     978123    adidas AG  DE000A1EWWW0        10-Q   2024-07-15   filings/DE/adidas/978123.md
3     979500    adidas AG  DE000A1EWWW0         8-K   2024-08-01   filings/DE/adidas/979500.md
```

**2. Find all documents of a specific type (e.g., all Annual Reports):**

```bash
python parse_metadata.py --filing-type 10-K
```

**Expected Output:**

```
Loading metadata from 'sample_metadata.jsonl'...
Found 2 documents for filing type '10-K':
--------------------------------------------------
   filing_id company_name company_isin filing_type release_date              local_file_path
0     974971    adidas AG  DE000A1EWWW0        10-K   2024-04-30  filings/DE/adidas/974971.md
2     975300       SAP SE  DE0007164600        10-K   2024-04-28      filings/DE/sap/975300.md
```