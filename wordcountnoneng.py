from pyspark.sql import SparkSession
from spellchecker import SpellChecker
import re
import subprocess
import sys

# Install pyspellchecker if not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import spellchecker
except ImportError:
    install('pyspellchecker')

# Create a SparkSession
spark = SparkSession.builder \
    .appName("NonEnglishWordCount") \
    .getOrCreate()


input_file_path = "/Users/apurva/bigdatafiles/txt_02_hw02.txt"
lines = spark.read.text(input_file_path).rdd.map(lambda r: r[0])

# Define a function to extract words from each line
def extract_words(line):
    WORD_RE = re.compile(r"[^\W\d_]+")
    return WORD_RE.findall(line.lower())

# Split each line into words
words = lines.flatMap(extract_words)

# Initialize the SpellChecker
spell_checker = SpellChecker()

# Check if a word is non-English
def is_non_english(word):
    return word.lower() not in spell_checker

# Filter non-English words
non_english_words = words.filter(is_non_english)

# Map each non-English word to a tuple of (word, 1)
non_english_word_counts = non_english_words.map(lambda word: (word, 1))

# Reduce by key to get the count of each non-English word
non_english_word_counts = non_english_word_counts.reduceByKey(lambda x, y: x + y)

# Collect the results
results = non_english_word_counts.collect()

# Print the results
for word, count in results:
    print(word, count)

# Stop the SparkSession
spark.stop()
