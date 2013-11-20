#!/usr/bin/python
import sys

from itertools import product
from collections import OrderedDict

def main():
    # The DNA(?) string to parse
    string_file = open(sys.argv[1], 'r')
    string = string_file.readlines()[0]
    kmer_length = int(sys.argv[2])

    # Also could have been the following, but would not have guarneeted the order.
    # Since this is a smaller data set, I can sacrifice the performance for reproduceability.
    # ''.join(set(string))
    alphabet = ''.join(OrderedDict.fromkeys(string).keys())
    perms = [''.join(i) for i in product(alphabet,repeat=kmer_length)]
    
    words = {}
    max_word_count = 0

    for perm in perms:
        count = string.count(perm)
        max_word_count = max(count, max_word_count)

        if count > 0:
            words[perm] = count

    # This prints the kmers with count = to max_count
    frequent_words = [k for k, v in words.iteritems() if v is max_word_count]

    # This prints the 14 most frequent kmers
    result = ''
    for word in frequent_words:
        if len(result) > 0:
            result = result + ' ' + word
        else:
            result = word

    print result

    try:
        output_file = sys.argv[3]
        output = open(output_file, 'w')
        output.write(result)
        output.close()
    except:
        pass

if __name__ == "__main__":
    main()
