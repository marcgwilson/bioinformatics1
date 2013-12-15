#!/usr/bin/python
import sys
from collections import OrderedDict

def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    k = int(data[1].strip())
    m = k - 1
    dna_string = data[2].strip()

    kmers = {}
    for i in range(len(dna_string) - m):
        # print dna_string[i:i + k]
        # kmers.append(dna_string[i:i + m])
        key = dna_string[i:i + m]
        value = dna_string[i + 1:i + m + 1]

        if key in kmers:
            kmers[key].append(value)
        else:
            kmers[key] = [value]

    ordered_kmers = OrderedDict(sorted(kmers.items()))

    # print ordered_kmers
    output = []

    for k in ordered_kmers:
        v = ordered_kmers[k]
        v.sort()
        joined_values = ','.join(v)
        output.append('%s -> %s' % (k, joined_values))

    result = '\n'.join(output)
    print result
    

if __name__ == "__main__":
    main()