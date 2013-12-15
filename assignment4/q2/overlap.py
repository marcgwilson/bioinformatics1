#!/usr/bin/python
import sys

def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    patterns = []

    for d in data:
        patterns.append(d.strip())

    overlaps = []
    for i in range(len(patterns)):
        p_i = patterns[i]
        for j in range(len(patterns)):
            if i != j:
                p_j = patterns[j]

                if p_i[1:len(p_i)] == p_j[0:len(p_j) -1]:
                    overlaps.append('%s -> %s' % (p_i, p_j))

    overlaps.sort()
    result = '\n'.join(overlaps)
    print result
    

if __name__ == "__main__":
    main()