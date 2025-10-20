![FinancialReports Logo](https://cdn.financialreports.eu/financialreports/static/assets/logo.svg)

# FinancialReports Code Examples (Cookbook)

Welcome to the official FinancialReports code examples repository. This "cookbook" provides clients and developers with practical, production-ready scripts to accelerate integration with:

1.  The FinancialReports REST API
2.  FinancialReports data dumps

## Repository Structure

This repository is organized into self-contained examples. The main categories are:

* `/api-examples`: Recipes for interacting with the FinancialReports API.
    * `/filings`: Examples for fetching and searching filings.
    * `/companies`: Examples for fetching company data.
* `/data-dump-processing`: Scripts for parsing and managing bulk data dumps.
    * `/text-extraction`: Examples for extracting text from document files.
    * `/metadata-parsing`: Examples for reading and filtering bulk metadata.
* `/common`: Shared utility functions or modules that might be used across multiple examples (e.g., advanced API client configurations).

## Getting Started

### 1. Find Your Example

Navigate into the example folder that matches your goal. For instance:
`cd api-examples/filings/get_latest_filings`

### 2. Install Dependencies

Each example is isolated and has its own `requirements.txt`:
`pip install -r requirements.txt`

### 3. Set Your API Key

All API scripts use an environment variable for security. **Never hardcode your API key.**

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_api_key_here"
```

### 4. Run the Script

`python example_script_name.py`

## Links

* **Main Website:** [https://financialreports.eu/](https://financialreports.eu/)
* **API Documentation:** [https://docs.financialreports.eu/](https://docs.financialreports.eu/)
* **Python SDK (PyPI):** [https://pypi.org/project/financial-reports-generated-client/](https://pypi.org/project/financial-reports-generated-client/)