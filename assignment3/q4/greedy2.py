#!/usr/bin/python
import sys

def score_motifs_count_matrix(motifs, profile, key_index, k):
    results = []

    for motif in motifs:
        max_probability = 0 #1.0
        selected_kmer = ''
        # print 'motif: %s' % motif
        for i in range(0, len(motif) - k + 1):
            kmer = motif[i:i+k]
            prob = 0 #1

            build_str = ''

            for j in range(0, len(kmer)):
                char = kmer[j]
                build_str += char
                index = key_index[char]

                # if kmer == 'CAA':
                #     print 'char: %s, percent: %s' % (char, profile[index][i + j])
                # print 'profile[index]: %s' % profile[index]
                # prob *= profile[index][i + j]
                prob += profile[index][j]

            # print 'kmer: %s prob: %s, build_str: %s' % (kmer, prob, build_str)
            # print '---'
            # print 'prob: %s, kmer: %s' % (prob, kmer)
            if prob > max_probability:
                max_probability = prob
                selected_kmer = kmer
        print 'max_probability: %s, selected_kmer: %s' % (max_probability, selected_kmer)
        results.append(selected_kmer)

    result = ' '.join(results)
    print result

# We need a list of pairs:
# The index of the pair corresponds to the row of the motif matrix
# The pair consists of a kmer and it's score
# For each iteration, add another row to the count matrix and recompute the profile matrix
# Then iterate over each row in the motif matrix and rescore each row. If a kmer has a higher score than the current kmer, replace that kmer, score pair

# One question I do have, is do I score every row of the motif matrix on every iteration? I think so.

def update_profile_matrix(motif, count_matrix, key_index):
    pass


def score_motifs_mult(motifs, profile, key_index, k):
    results = []

    for motif in motifs:
        max_probability = -1.0
        selected_kmer = ''
        # print 'motif: %s' % motif
        for i in range(0, len(motif) - k + 1):
            kmer = motif[i:i+k]
            prob = float(1.0)

            build_str = ''

            for j in range(0, len(kmer)):
                char = kmer[j]
                build_str += char
                index = key_index[char]

                # if kmer == 'CAA':
                #     print 'char: %s, percent: %s' % (char, profile[index][i + j])
                # print 'profile[index]: %s' % profile[index]
                # prob *= profile[index][i + j]
                prob *= profile[index][j]

            # print 'kmer: %s prob: %s, build_str: %s' % (kmer, prob, build_str)
            # print '---'
            # print 'prob: %s, kmer: %s' % (prob, kmer)
            if prob > max_probability:
                max_probability = prob
                selected_kmer = kmer

        results.append(selected_kmer)

    result = ' '.join(results)
    print result


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    k_t = data[1].strip().split(' ')
    k = int(k_t[0])
    t = int(k_t[1])

    key_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    motifs = []

    count = [[],[],[],[]]
    profile = [[],[],[],[]]

    for i in range(2, 2 + t):
        motif = data[i].strip()
        motifs.append(motif)

    motif_length = len(motifs[0])

    for i in range(0, min(t, motif_length)):
        # Give each column an initial value of 0
        for c in count:
            c.append(0)

        for motif in motifs:
            char = motif[i]
            index = key_index[char]
            count[index][i] = count[index][i] + 1

    for i in range(0, len(count[0])):
        s = 0
        for c in count:
            s += c[i]

        # Give each column an initial value of 0
        for p in profile:
            p.append(0)

        for j in range(0, len(count)):
            profile[j][i] = float(count[j][i]) / float(s)

    score_motifs_mult(motifs, profile, key_index, k)
    score_motifs_count_matrix(motifs, count, key_index, k)

if __name__ == "__main__":
    main()