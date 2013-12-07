#!/usr/bin/python
import sys

"""
source is the RNA to translate
codons is a string of RNA-peptide pairs 
"""
def translate(source, codon_list):
    # Build the codon dictionary
    codons = {}

    for c in codon_list:
        c = c.strip()
        pair = c.split(' ')

        if len(pair) == 2:
            codons[pair[0]] = pair[1]
        elif len(pair) == 1:
            codons[pair[0]] = ''

    # Perform the translation
    output_string = ''

    for i in xrange(0, len(source), 3):
        three_mer = source[i:(i + 3)]

        output_string = output_string + codons[three_mer]

    return output_string


def main():
    translation_file = open(sys.argv[1], 'r')
    translation_pairs = translation_file.readlines()
    string_file = open(sys.argv[2], 'r')
    strings = string_file.readlines()

    # Index 0 is 'Input'
    input_data = strings[0].strip()

    output_string = translate(input_data, translation_pairs)

    print output_string

    # try:
    #     # Index 2 is 'Output'
    #     output_data = strings[3].strip()

    #     if output_data == output_string:
    #         print 'PASS'
    #     else:
    #         print 'FAIL'
    # except:
    #     pass

if __name__ == "__main__":
    main()