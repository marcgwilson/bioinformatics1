#!/usr/bin/python
import sys
from itertools import product


def char_diff(first, second):
    count = 0

    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1

    return count


def distance(pattern, string):
    d = len(pattern) + 1

    for i in range(0, len(string) - len(pattern) + 1):
        substring = string[i:i+len(pattern)]
        diff = char_diff(pattern, substring)

        if diff < d:
            d = diff

    return d


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    k= int(data[1].strip())

    print 'k: %s' % k

    # Build a list of strings
    dna_strings_list = []

    for i in range(2, len(data) - 2):
        dna_string = data[i].strip()
        dna_strings_list.append(dna_string)

    alphabet = 'ACGT'
    perms = [''.join(i) for i in product(alphabet,repeat=k)]

    pattern_dict = {}

    for perm in perms:
        count = 0
        for string in dna_strings_list:
            # t = distance(perm, string)
            count += distance(perm, string)

        pattern_dict[perm] = count

    min_value = min(pattern_dict.itervalues())
    min_keys = [key for key in pattern_dict if pattern_dict[key] == min_value]

    result = ' '.join(min_keys)
    print result


if __name__ == "__main__":
    main()