#!/usr/bin/python
import sys

# Normalizes a count_matrix into a matrix of probabilities
def generate_profile_matrix(count_matrix):
    sum_list = [0] * len(count_matrix[0])
    
    for j in range(0, len(count_matrix[0])):
        for i in range(0, len(count_matrix)):
            sum_list[j] += count_matrix[i][j]

    profile_matrix = []

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


# This takes a list of motifs and builds a count matrix
def generate_count_matrix(motifs, key_index):
    count_matrix = []
    for c in range(0, 4):
        count_matrix.append([0] * len(motifs[0]))

    for motif in motifs:
        for i in range(len(motif)):
            char = motif[i]
            index = key_index[char]
            count_matrix[index][i] = count_matrix[index][i] + 1

    return count_matrix


def score(motifs, key_index, k, profile_matrix):
    scores = [['', -1.0] for i in range(len(motifs))]

    for m in range(len(motifs)):  # otif in motifs:
        motif = motifs[m]
        for i in range(len(motif) - k + 1):
            kmer = motif[i:i+k]
            prob = float(1.0)

            for j in range(0, len(kmer)):
                char = kmer[j]
                index = key_index[char]
                prob *= profile_matrix[index][j]

            if prob >= scores[m][1]:
                scores[m][0] = kmer
                scores[m][1] = prob

    return scores


def best_motifs(motifs, k):
    key_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    scores = [['', -1.0] for i in range(len(motifs))]

    # Build the initial count matrix by selecting the first kmer in each of the motifs
    best = []
    for motif in motifs:
        best.append(motif[0:k])

    initial_count_matrix = generate_count_matrix(best, key_index)
    initial_profile_matrix = generate_profile_matrix(initial_count_matrix)
    initial_scores = score(motifs, key_index, k, initial_profile_matrix)

    for i in range(len(best)):
        best[i] = initial_scores[i][0]
        count_matrix = generate_count_matrix(best, key_index)
        profile_matrix = generate_profile_matrix(count_matrix)
        scores = score(motifs, key_index, k, profile_matrix)
    
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

    result = ''
    for score in scores:
        result += '%s\n' % score[0]

    print result


if __name__ == "__main__":
    main()