#!/usr/bin/python
import sys
from collections import OrderedDict


# Returns a lits of kmers from the loaded data
def build_kmer_list(data):
    kmers = []
    for d in data:
        d = d.strip()
        if d != 'Output:':
            kmers.append(d)
        else:
            break
    return kmers


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    kmer_list = build_kmer_list(data[1:])

    edges = []
    for kmer in kmer_list:
        edges.append([kmer[:-1], kmer[1:]])

    print edges

    graph = {}
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

    # print 'graph: %s' % graph

    ordered_kmers = OrderedDict(sorted(graph.items()))

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