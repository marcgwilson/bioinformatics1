#!/usr/bin/python
import sys
# from itertools import product


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

    dna_string = data[1].strip()

    k= int(data[2].strip())
    # keys = data[3].strip().split(' ')

    matrix = [[],[],[],[]]

    # Read the next k lines to build the profile matrix
    for i in range(4, 4 + k):
        row = data[i].strip().split(' ')
        for j in range(0, len(row)):
            matrix[j].append(float(row[j]))

    key_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    p = {}

    for i in range(0, len(dna_string) - k + 1):
        s = dna_string[i:i+k]
        prob = 1

        for j in range(0, len(s)):
            prob *= matrix[key_index[s[j]]][j]

        p[s] = prob

    max_value = max(p.itervalues())
    max_keys = [key for key in p if p[key] == max_value]

    result = ' '.join(max_keys)
    print result


if __name__ == "__main__":
    main()