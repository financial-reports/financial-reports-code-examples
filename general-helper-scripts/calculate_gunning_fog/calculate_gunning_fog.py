import sys
import argparse
import re

def calculate_gunning_fog(filepath: str):
    """
    Calculates the Gunning fog index for a given text file.
    
    Index = 0.4 * ( (words / sentences) + 100 * (complex_words / words) )
    """
    
    print(f"Analyzing '{filepath}'...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    if not text:
        print("File is empty, nothing to analyze.")
        sys.exit(0)

    # 1. Count Sentences
    # Find sentences ending in . ! ? or newline
    sentences = re.split(r'[.!?\n]+', text)
    # Filter out empty strings that result from split
    sentences = [s for s in sentences if s.strip()]
    num_sentences = len(sentences)
    
    if num_sentences == 0:
        print("No complete sentences found in the text.")
        sys.exit(0)

    # 2. Count Words
    # Find all words (sequences of letters)
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    num_words = len(words)
    
    if num_words == 0:
        print("No words found in the text.")
        sys.exit(0)

    # 3. Count Complex Words (3+ syllables)
    num_complex_words = 0
    for word in words:
        if count_syllables(word) >= 3:
            num_complex_words += 1
            
    # 4. Perform Calculation
    avg_sentence_length = num_words / num_sentences
    percent_complex_words = (num_complex_words / num_words) * 100
    
    gunning_fog_index = 0.4 * (avg_sentence_length + percent_complex_words)

    # --- Print the results ---
    print("--------------------------------")
    print(f"Total Sentences: {num_sentences}")
    print(f"Total Words: {num_words}")
    print(f"Total Complex Words: {num_complex_words}")
    print("--------------------------------")
    print(f"Average Sentence Length: {avg_sentence_length:.2f}")
    print(f"Percentage of Complex Words: {percent_complex_words:.2f}%")
    print("--------------------------------")
    print(f"Gunning Fog Index: {gunning_fog_index:.2f}")


def count_syllables(word: str) -> int:
    """
    A simple heuristic-based syllable counter for English.
    """
    # Lowercase the word
    word = word.lower()
    
    # Handle common exceptions
    if len(word) <= 3:
        return 1
    
    # Remove silent 'e' at the end
    if word.endswith('e') and not word.endswith('le'):
        word = word[:-1]
        
    # Count vowel groups (a, e, i, o, u, y)
    vowel_groups = re.findall(r'[aeiouy]+', word)
    
    # Default to 1 if no vowel groups found (e.g., "rhythm")
    syllable_count = max(1, len(vowel_groups))
    
    return syllable_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the Gunning fog index for a text file."
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Path to the text file to analyze."
    )
    
    args = parser.parse_args()
    
    calculate_gunning_fog(args.file)