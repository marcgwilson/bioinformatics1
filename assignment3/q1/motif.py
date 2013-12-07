#!/usr/bin/python
import sys
from itertools import product

def chars_in_common(first, second):
    count = 0

    if len(first) != len(second):
        return count

    for i in range(len(first)):
        if first[i] == second[i]:
            count = count + 1

    return count

def char_diff(first, second):
    count = 0

    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1

    return count

def motif_enumeration(dna, k, d):
    pass


def mutations(perms, kmer, d):
    m = []

    for perm in perms:
        if char_diff(perm, kmer) <= d:
            m.append(perm)

    return m


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    kmer_mutation = data[1].split(' ')
    # print 'string_list: %s' % string_list
    kmer_length = int(kmer_mutation[0])
    mutation_count = int(kmer_mutation[1])

    alphabet = 'ACGT'
    perms = [''.join(i) for i in product(alphabet,repeat=kmer_length)]

    mutation_set = set()

    for i in range(2, len(data) - 2):
        dna_string = data[i].strip()
        # print dna_string
        for j in range(0, len(dna_string) - kmer_length + 1):
            kmer = dna_string[j:j+kmer_length]
            m = mutations(perms, kmer, mutation_count)
            mutation_set = mutation_set.union(set(m))

    result_list = []

    for mutation in mutation_set:
        string_count = len(data) - 2 - 2
        count = 0
        for i in range(2, len(data) - 2):
            dna_string = data[i].strip()

            for j in range(0, len(dna_string) - kmer_length + 1):
                kmer = dna_string[j:j+kmer_length]
                found = False

                if char_diff(kmer, mutation) <= mutation_count:
                    found = True

                if found:
                    count+=1
                    break

        if count == string_count:
            result_list.append(mutation)

    result = ' '.join(result_list)
    print result


if __name__ == "__main__":
    main()