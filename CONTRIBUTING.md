# Contribution Guidelines

To maintain a high standard of quality and usability, all contributions to this repository must follow these guidelines.

## The Golden Rule: Self-Contained Examples

Every example script *must* be self-contained in its own directory. A user must be able to `cd` into any example folder, follow its `README`, and have it work.

### Example Folder Structure

```text
/example-category/parse-metadata-csv/
├── README.md         (Instructions specific to this script)
├── parse_script.py   (The Python script)
└── requirements.txt  (Minimal dependencies for this script)
```

### 1. README.md (Per Example)

The `README.md` for each example is mandatory and must include:

* A clear title and purpose (e.g., "Example: Parse Data Dump Metadata").
* A `Setup` section (e.g., `pip install -r requirements.txt`).
* An `Authentication` section (if it hits the API), instructing the user to set the `FR_API_KEY` environment variable.
* A `Usage` section (e.g., `python parse_script.py --input-file /path/to/metadata.jsonl`).
* An `Expected Output` section (a small snippet of the console output).

### 2. requirements.txt (Per Example)

* This file must list all non-standard-library dependencies.
* It should be minimal. Do not add `pandas` if it's not required for that specific script.
* Even if no dependencies are needed, an empty `requirements.txt` file should be included for consistency.

### 3. Code Standards

* **Security**: API keys MUST be read from the environment. Use `os.environ.get("FR_API_KEY")`. Scripts must fail gracefully with an error message if the key is not set.
* **API Scripts**: Must use the `financial-reports-generated-client` SDK. Do not use raw `requests` unless the SDK does not support the endpoint.
* **Data Processing**: `pandas` is the preferred library for any scripts that parse or manipulate data (e.g., from `.jsonl` or `.csv` files).
* **Style**: Follow PEP 8 guidelines.
* **Error Handling**: Include basic `try...except` blocks for API calls or file I/O.