# Word Count and Non-English Word Filtering using MapReduce

## Overview
This repository contains two tasks for word processing using the MapReduce framework.

### Task 1: Word Count in a Text File
Using MapReduce, we count the number of occurrences of each word in a text file.

### Task 2: Count Non-English Words
For Task 2, MapReduce is applied to count the occurrences of non-English words in the text file. 

## Files

- **mapreduce_wordcount.py**: This file contains the MapReduce implementation for counting the number of occurrences of each word.
- **mapreduce_non_english.py**: This file includes the MapReduce logic to filter and count non-English words.

## How to Run

1. Clone the repository.
2. Place the text file (e.g., `harry_potter.txt`) in the same directory.
3. Execute the scripts:

```bash
python3 mapreduce_wordcount.py
python3 mapreduce_non_english.py
