# Example: Count Keywords (ESG Theme)

This script is a general-purpose helper that reads a text or markdown file and counts the occurrences of a predefined list of keywords.

For this example, the script is pre-configured with a list of common **ESG (Environmental, Social, and Governance)** terms. This is a common task in financial analysis to gauge a report's focus on ESG topics.

The script performs a case-insensitive search and uses word boundaries to ensure "ghg" doesn't match "ghg_emissions" (which would be counted separately).

## Setup

This script uses only built-in Python libraries, but our standard pattern is to create an environment and install dependencies.

```bash
# No dependencies to install, but good practice
pip install -r requirements.txt
```

## Run

The script takes one required argument:

* `--file`: The path to the file you want to analyze.

Example Command (using our sample):

```bash
python count_keywords.py --file sample_report.md
```

## Expected Output

The script will print a count for each keyword found in the file (counts will vary based on your `sample_report.md`):

```
Analyzing 'sample_report.md' for ESG keywords...
Found 15 total keyword mentions.
--------------------------------------------------
Environmental:
- climate change: 5
- emissions: 3
- ghg: 2
- renewable: 1
- sustainability: 2

Social:
- diversity: 1
- employee well-being: 1
- human rights: 0
- inclusion: 0

Governance:
- board independence: 0
- executive compensation: 0
- shareholder rights: 0
```