#!/usr/bin/python
import sys

from itertools import product
from collections import OrderedDict

def chars_in_common(first, second):
    count = 0

    if len(first) != len(second):
        return count

    for i in range(len(first)):
        if first[i] == second[i]:
            count = count + 1

    return count

def main():
    # The DNA(?) string to parse
    string_file = open(sys.argv[1], 'r')
    data = string_file.readlines()
    string_list = data[1].split(' ')
    # print 'string_list: %s' % string_list
    string = string_list[0]
    kmer_length = int(string_list[1])
    mismatches = int(string_list[2])
    in_common = kmer_length - mismatches

    print 'string: %s, kmer_length: %s, mismatches: %s' % (string, kmer_length, mismatches)
    # Also could have been the following, but would not have guarneeted the order.
    # Since this is a smaller data set, I can sacrifice the performance for reproduceability.
    # ''.join(set(string))
    alphabet = ''.join(OrderedDict.fromkeys(string).keys())
    perms = [''.join(i) for i in product(alphabet,repeat=kmer_length)]
    
    # words = {}
    words = []

    max_count = 0

    for perm in perms:
        total_mismatch = 0

        for i in range(0, len(string) - kmer_length):
            substring = string[i:(i+kmer_length)]

            if chars_in_common(perm, substring) >= in_common:
                total_mismatch = total_mismatch + 1

        if total_mismatch > max_count:
            max_count = total_mismatch
            words = [perm, ]
        elif total_mismatch == max_count:
            words.append(perm)

    result = ' '.join(words)
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