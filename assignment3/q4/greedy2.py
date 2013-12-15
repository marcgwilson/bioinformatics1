#!/usr/bin/python
import sys

# We need a list of pairs:
# The index of the pair corresponds to the row of the motif matrix
# The pair consists of a kmer and it's score
# For each iteration, add another row to the count matrix and recompute the profile matrix
# Then iterate over each row in the motif matrix and rescore each row. If a kmer has a higher score than the current kmer, replace that kmer, score pair

# One question I do have, is do I score every row of the motif matrix on every iteration? I think so.
# List multiplication can create lists of length N with a default value v
# default_list = [v] * N
# eg, default_list = [0] * 4 = [0, 0, 0, 0]
#

# Normalizes a count_matrix into a matrix of probabilities
def generate_profile_matrix(count_matrix):
    print 'count_matrix: %s' % count_matrix
    sum_list = [0] * len(count_matrix[0])
    
    for j in range(0, len(count_matrix[0])):
        for i in range(0, len(count_matrix)):
            sum_list[j] += count_matrix[i][j]

    profile_matrix = []
    print 'sum_list: %s' % sum_list
    for k in range(0, 4):
        profile_matrix.append([0] * len(count_matrix[0]))

    for i in range(0, len(count_matrix)):
        for j in range(0, len(count_matrix[i])):
            profile_matrix[i][j] = float(count_matrix[i][j]) / float(sum_list[j])

    return profile_matrix


def build_motif(data):
    motifs = []

    for i in range(0, len(data)):
        motif = data[i].strip()
        motifs.append(motif)

    return motifs


def build_count_matrix(motifs, t, k, key_index):
    count_matrix = []
    for c in range(0, 4):
        count_matrix.append([0] * k)

    for depth in range(0, t + 1):
        motif = motifs[depth] 

        for i in range(k):
            char = motif[i]
            index = key_index[char]
            count_matrix[index][i] = count_matrix[index][i] + 1

    return count_matrix


def best_motifs(motifs, k):
    key_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    scores = [['', -1.0] for i in range(len(motifs))]
    # print 'scores: %s' % scores

    # it_count = 0
    for m in range(0, len(motifs)):
        count = build_count_matrix(motifs, m, k, key_index)
        profile = generate_profile_matrix(count)
        # print 'it_count: %s, profile: %s\n' % (it_count, profile)
        m = 0
        for motif in motifs:
            for i in range(len(motif) - k + 1):
                kmer = motif[i:i+k]
                prob = float(1.0)

                for j in range(0, len(kmer)):
                    char = kmer[j]
                    index = key_index[char]
                    prob *= profile[index][j]

                if prob >= scores[m][1]:
                    scores[m][0] = kmer
                    scores[m][1] = prob
            m+=1
        # it_count+=1
    
    return scores


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    k_t = data[1].strip().split(' ')
    k = int(k_t[0])
    t = int(k_t[1])

    motifs = build_motif(data[2:2 + t])
    scores = best_motifs(motifs, k)
    # print 'scores: %s' % scores

    result = ''
    for score in scores:
        result += '%s\n' % score[0]

    print result


if __name__ == "__main__":
    main()