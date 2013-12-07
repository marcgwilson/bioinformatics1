#!/usr/bin/python
import sys

"""
codon_list is a string of RNA-peptide pairs 
"""
def build_codon_dict(codon_list):
    codons = {}

    for c in codon_list:
        c = c.strip()
        pair = c.split(' ')

        if len(pair) == 2:
            codons[pair[0]] = pair[1]
        elif len(pair) == 1:
            codons[pair[0]] = ''

    return codons


"""
source is the RNA to translate
codons is a dictionary of RNA-peptide pairs
"""
def translate(source, codons):
    # Perform the translation
    output_string = ''

    for i in xrange(0, len(source), 3):
        three_mer = source[i:(i + 3)]

        try:
            codon = codons[three_mer]
        except:
            codon = ''

        output_string = output_string + codon

    return output_string

# This function replaces each nucleotide with it's compliment and reverses the string as it is built
def inverse(source):
    inv = ''

    for i in range(0, len(source)):
        char = source[i]

        if char == 'G':
            inv = 'C' + inv
        elif char == 'C':
            inv = 'G' + inv
        elif char == 'U':
            inv = 'A' + inv
        elif char == 'A':
            inv = 'U' + inv

    return inv


def search(dna, codon_list, peptide):
    codons = build_codon_dict(codon_list)
    peptide_length = len(peptide)

    # print 'peptide_length: %s' % peptide_length

    for i in range(0, len(dna)):
        substr = dna[i:(i + 3 * peptide_length)]
        result = translate(substr, codons)
        inverse_result = translate(inverse(substr), codons)

        if result == peptide or inverse_result == peptide:
            print substr.replace('U', 'T')


def main():
    translation_file = open(sys.argv[1], 'r')
    translation_pairs = translation_file.readlines()
    string_file = open(sys.argv[2], 'r')
    strings = string_file.readlines()

    # Index 0 is 'Input'
    input_data = strings[1].strip().replace('T', 'U')
    peptide = strings[2].strip()

    # rna = 'GTAGTAATGGGGCTCAAACACCTCTTT'.replace('T', 'U')
    # rna_r = rna[::-1]
    # pep = translate(rna, build_codon_dict(translation_pairs)).replace('U', 'T')
    # pep_r = translate(rna_r, build_codon_dict(translation_pairs)).replace('U', 'T')

    # print 'pep: %s' % pep
    # print 'pep_r: %s' % pep_r
    # print 'input_data: %s, peptide: %s, translation_pairs: %s' % (input_data, peptide, translation_pairs)

    search(input_data, translation_pairs, peptide)


if __name__ == "__main__":
    main()