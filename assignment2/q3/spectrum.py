#!/usr/bin/python
import sys
from collections import OrderedDict

def compute_masses(peptide, mass_table):
    # l is the length of the sub-peptide

    # d = {}
    a = []

    for l in range(1, len(peptide)):
        for i in range(0, len(peptide)):

            kmer = peptide[i:min(i + l, len(peptide))]

            if (i + l) > len(peptide):
                kmer = kmer + peptide[0:l - len(kmer)]

            # now compute the kmer's mass
            weight = 0
            for j in range(0, len(kmer)):
                weight = weight + int(mass_table[kmer[j]])

            # d[kmer] = weight
            a.append(weight)

    weight = 0
    for k in range(0, len(peptide)):
        weight = weight + int(mass_table[peptide[k]])

    # d[peptide] = weight
    a.append(weight)

    # s = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

    a.sort()

    ret = '0'
    for b in a:
        ret = '%s %s' % (ret, b)
    # for v in s.values():
    #     ret = '%s %s' % (ret, v)

    print ret


def build_mass_table(mass_list):
    masses = {}

    for m in mass_list:
        m = m.strip()
        pair = m.split(' ')
        masses[pair[0]] = pair[1]

    return masses

def main():
    mass_file = open(sys.argv[1], 'r')
    mass_data = mass_file.readlines()

    mass_table = build_mass_table(mass_data)

    print 'mass_table: %s' % mass_table

    string_file = open(sys.argv[2], 'r')
    strings = string_file.readlines()

    # Index 0 is 'Input'
    input_data = strings[1].strip()

    print 'input: %s' % input_data

    compute_masses(input_data, mass_table)


if __name__ == "__main__":
    main()