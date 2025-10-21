![FinancialReports Logo](https://cdn.financialreports.eu/financialreports/static/assets/logo.svg)
# The FinancialReports Code Cookbook

Welcome to the official FinancialReports code cookbook. This repository provides practical, production-ready solutions to accelerate your financial data analysis. Our goal is to help you go from raw data to actionable insights in minutes.

This "cookbook" provides clients and developers with scripts and notebooks to accelerate integration with:

1.  **The FinancialReports REST API**
2.  **FinancialReports Data Dumps**

## How to Use This Cookbook

1.  **Start with the Basics:** If you're new, begin with our `00_Getting_Started.ipynb` notebook.
2.  **Find Your Goal:** Browse the **Recipe Index** below to find the category that matches your problem.
3.  **Explore the Examples:** Click the link to navigate to the relevant directory and explore the self-contained examples inside.

Every example has its own `README.md` with specific instructions.

---

## Recipe Index

| Goal / Use Case | Explore Recipes In | Description |
| :--- | :--- | :--- |
| **Start Here: Learn the Basics** | **[`00_Getting_Started.ipynb`](./00_Getting_Started.ipynb)** | Learn how to set your API key, make your first API calls, and handle responses. |
| **Solve a Real-World Problem** | **[`/use-cases/`](./use-cases/)** | Advanced workflows that combine multiple tools to solve complex problems like competitor analysis or bulk readability scoring. |
| **Process a Large Data Dump** | **[`/data-dump-processing/`](./data-dump-processing/)** | Production-ready scripts to handle bulk data, like loading a huge CSV into a high-performance SQLite database. |
| **Analyze Filing Content** | **[`/analysis/`](./analysis/)** | Standalone notebooks for specific analytical tasks like calculating readability (Gunning Fog) or counting keyword mentions. |
| **Find a Simple API Snippet** | **[`/api-examples/`](./api-examples/)** | A collection of basic, standalone Python scripts for individual API endpoints (e.g., get a company, search filings). |

---

## Authentication

For all examples that use the API, you must set your API key as an environment variable. **Never hardcode your key.**

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_api_key_here"
```

## Links & Support

* **Main Website**: https://financialreports.eu/
* **API Documentation**: https://docs.financialreports.eu/
* **Python SDK (PyPI)**: https://pypi.org/project/financial-reports-generated-client/
* **Support**: Contact `support@financialreports.eu` for questions.

## Contributing

We welcome contributions! Please see our updated `CONTRIBUTING.md` file for detailed guidelines on code standards and our preference for Jupyter Notebooks for analysis.