# Contribution Guidelines

To maintain a high standard of quality and usability, all contributions to this repository must follow these guidelines.

## The Golden Rule: Self-Contained Examples

Every example *must* be self-contained in its own directory. A user must be able to `cd` into any example folder, follow its `README.md`, and have it work without dependencies from other folders (except for importing from an established `utils.py` in another analysis example).

### Example Folder Structure

```text
/example-category/example-name/
├── README.md         (Instructions specific to this example)
├── example.ipynb     (The Jupyter Notebook, if applicable)
├── example_script.py (The Python script, if applicable)
└── requirements.txt  (Minimal dependencies for this example)
```

### Notebooks vs. Scripts: Which to Choose?

We use both Python scripts (`.py`) and Jupyter Notebooks (`.ipynb`). Choose the right tool for the job.

**Use Jupyter Notebooks (`.ipynb`) for:**

* **Tutorials & Getting Started Guides:** Anything that teaches a concept step-by-step.
* **Analysis & Visualization (`/analysis`):** Any example where the goal is to explore data, calculate a metric, or show a plot.
* **Workflows & Use Cases (`/use-cases`):** All multi-step workflows that combine API calls or analysis techniques.

**Use Python Scripts (`.py`) for:**

* **Production-Style Tasks:** Examples intended to be run repeatedly as a command-line tool, especially for data processing (e.g., `/data-dump-processing/load_metadata_csv_to_sqlite`).

### Notebook Guidelines

* **Explain the "Why"**: Use Markdown cells extensively to explain what the code is doing and why it's useful.
* **Keep Cells Short**: Each code cell should perform one logical action.
* **Ensure Top-to-Bottom Execution**: The notebook must run cleanly from the first cell to the last without errors.
* **No Hardcoded Keys**: API keys must be loaded from the environment. Do not save a notebook with a key visible in the code.

### Script Guidelines

* **Security**: API keys MUST be read from the environment. Use `os.environ.get("FR_API_KEY")`. Scripts must fail gracefully with an error message if the key is not set.
* **Command-Line Arguments**: Use `argparse` for any user-configurable parameters like input files or flags.
* **API Scripts**: Must use the `financial-reports-generated-client` SDK. Do not use raw `requests` unless the SDK does not support the endpoint.
* **Style**: Follow PEP 8 guidelines.
* **Error Handling**: Include basic `try...except` blocks for API calls or file I/O.