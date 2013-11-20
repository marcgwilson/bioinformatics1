#!/usr/bin/python
import sys

def main():
    string_file = open(sys.argv[1], 'r')
    strings = string_file.readlines()
    string = strings[0].rstrip()
    numbers = strings[1].rstrip().split(' ')

    k = int(numbers[0])
    L = int(numbers[1])
    t = int(numbers[2])

    clumped_kmers = set()

    result = ''

    for i in range(0, (len(string) - L)):
        substring = string[i:(i + L)]

        kmers = {}
        for j in range(0, (len(substring) - k)):
            kmer = substring[j:(j + k)]
            if kmer in kmers:
                kmers[kmer] = kmers[kmer] + 1
            else:
                kmers[kmer] = 1

        frequent_kmers = set(key for key, value in kmers.iteritems() if value >= t)
        clumped_kmers = clumped_kmers.union(frequent_kmers)


    result = ' '.join(clumped_kmers)
    print result

    try:
        output_file = sys.argv[2]
        output = open(output_file, 'w')
        output.write(result)
        output.close()
    except:
        pass

if __name__ == "__main__":
    main()