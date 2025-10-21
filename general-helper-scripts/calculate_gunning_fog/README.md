# Example: Calculate Gunning Fog Index

This script is a general-purpose helper that calculates the **Gunning fog index** for a given text file. This index is a common metric used to estimate the readability of a text, corresponding to the years of formal education needed to understand it.

## The Formula

The script uses the standard Gunning fog formula:

`Index = 0.4 * ( (Average Sentence Length) + (Percentage of Complex Words) )`

* **Average Sentence Length:** Total words / Total sentences.
* **Complex Words:** Words with 3 or more syllables.

## Setup

This script uses only built-in Python libraries.

```bash
# No dependencies to install
pip install -r requirements.txt
```

## Run

The script takes one required argument:

* `--file`: The path to the text file you want to analyze.

Example Command (using our sample):

```bash
python calculate_gunning_fog.py --file sample_text.txt
```

## Expected Output

The script will print the core statistics and the final calculated index score (the exact numbers will depend on the `sample_text.txt`).

```
Analyzing 'sample_text.txt'...
--------------------------------
Total Sentences: 6
Total Words: 105
Total Complex Words: 11
--------------------------------
Average Sentence Length: 17.50
Percentage of Complex Words: 10.48%
--------------------------------
Gunning Fog Index: 11.19
```