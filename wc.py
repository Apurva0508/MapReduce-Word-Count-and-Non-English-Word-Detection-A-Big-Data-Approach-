
from mrjob.job import MRJob
import re
import sys

# Modified regular expression to match only words without numbers and special characters
WORD_RE = re.compile(r"[^\W\d_]+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            # Emit each word with a count of 1
            yield word.lower(), 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
