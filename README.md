# Word Count and Non-English Word Filtering using MapReduce

## Overview
This repository contains two tasks for word processing using the MapReduce framework.

### Task 1: Word Count in a Text File
Using MapReduce, we count the number of occurrences of each word in a text file.

### Task 2: Count Non-English Words
For Task 2, MapReduce is applied to count the occurrences of non-English words in the text file. 

## Files


1. wc.py
This file implements a basic MapReduce logic for counting the occurrence of each word in a text file.

2. wordcount.py
A more comprehensive MapReduce implementation, which reads a text file, breaks it into tokens (words), and outputs the word count for each unique word.

3. wordcountnoneng.py
This script is designed to count the number of occurrences of non-English words using a predefined list of English words. It uses the MapReduce framework similar to the previous scripts but filters out words present in the English word list.

4. ouput.log
This log file contains the output from running the wc.py script, which includes the word count for the provided input text file.

5. outputnoneng.log
This log file contains the output from running the wordcountnoneng.py script, which lists non-English words along with their respective counts.

## How to Run

1. Clone the repository.
2. Place the text file (e.g., `harry_potter.txt`) in the same directory.
3. Execute the scripts:


