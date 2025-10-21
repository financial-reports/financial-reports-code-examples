# analysis/calculate_gunning_fog/utils.py

import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# --- Ensure NLTK data is available ---
# The user will be prompted to download this in the notebook,
# but having a fallback here is good practice.
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    print("NLTK 'punkt' tokenizer not found. Please run the setup in the accompanying notebook.")
    # In a real library, you might trigger the download here, but for a cookbook,
    # instructing the user is better.

def is_complex_word(word: str) -> bool:
    """
    Determines if a word is "complex" (3 or more syllables).
    This is a heuristic and may not be perfect for all English words.
    """
    # 1. Lowercase the word
    word = word.lower()

    # 2. Remove non-alphabetic characters
    word = re.sub(r'[^a-z]', '', word)
    if not word:
        return False

    # 3. Exception for common suffixes that don't add a syllable
    if word.endswith(('es', 'ed', 'ing')):
        word = word[:-2] if word.endswith('es') else word[:-2] if word.endswith('ed') else word[:-3]

    # 4. Count vowel groups to estimate syllables
    vowels = "aeiouy"
    syllable_count = 0
    if word and word[0] in vowels:
        syllable_count += 1
    
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            syllable_count += 1
            
    # A single-letter word is one syllable
    if len(word) == 1 and syllable_count == 0:
        syllable_count = 1

    return syllable_count >= 3


def calculate_gunning_fog(text: str) -> float:
    """
    Calculates the Gunning Fog Index for a given text.
    Formula: 0.4 * ( (words / sentences) + 100 * (complex_words / words) )
    """
    if not text.strip():
        return 0.0

    # 1. Tokenize sentences and words
    sentences = sent_tokenize(text)
    words = [word for word in word_tokenize(text) if word.isalpha()]

    if not sentences or not words:
        return 0.0

    # 2. Calculate average words per sentence
    avg_words_per_sentence = len(words) / len(sentences)

    # 3. Calculate percentage of complex words
    complex_words = [word for word in words if is_complex_word(word)]
    percentage_complex_words = (len(complex_words) / len(words)) * 100

    # 4. Apply the Gunning Fog formula
    fog_index = 0.4 * (avg_words_per_sentence + percentage_complex_words)

    return fog_index