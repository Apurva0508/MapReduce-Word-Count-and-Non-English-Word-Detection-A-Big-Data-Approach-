from pyspark.sql import SparkSession
import re

# Create a SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read the input text file
lines = spark.read.text("/Users/apurva/bigdatafiles/text_01_hw02.txt").rdd.map(lambda r: r[0])

# Define a function to extract words from each line
def extract_words(line):
    WORD_RE = re.compile(r"[^\W\d_]+")
    return WORD_RE.findall(line.lower())

# Split each line into words
words = lines.flatMap(extract_words)

# Map each word to a tuple of (word, 1)
word_counts = words.map(lambda word: (word, 1))

# Reduce by key to get the count of each word
word_counts = word_counts.reduceByKey(lambda x, y: x + y)

# Collect the results
results = word_counts.collect()

# Print the results
for word, count in results:
    print(word, count)

# Stop the SparkSession
spark.stop()
