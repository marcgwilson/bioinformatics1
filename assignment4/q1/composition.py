#!/usr/bin/python
import sys

def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    k = int(data[1].strip())
    dna_string = data[2].strip()

    kmers = []
    for i in range(len(dna_string) - k + 1):
    	# print dna_string[i:i + k]
    	kmers.append(dna_string[i:i + k])

    kmers.sort()

    result = '\n'.join(kmers)
    print result
    

if __name__ == "__main__":
    main()