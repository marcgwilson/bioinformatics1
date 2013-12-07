#!/usr/bin/python
import sys
# import itertools

from itertools import product
from collections import OrderedDict

def chars_in_common(first, second):
    count = 0

    if len(first) != len(second):
        return count

    for i in range(len(first)):
        if first[i] == second[i]:
            count = count + 1

    return count


def mismatch_count(first, second):
    count = 0

    if len(first) != len(second):
        print 'first: %s, second: %s' % (first, second)
        raise Exception

    for i in range(len(first)):
        if first[i] != second[i]:
            count = count + 1
    return count


def mismatch_indices(first, second):
    indices = []

    if len(first) != len(second):
        print 'first: %s, second: %s' % (first, second)
        raise Exception

    for i in range(len(first)):
        if first[i] != second[i]:
            indices.append(i)
    return indices

def main():
    # The DNA(?) string to parse
    string_file = open(sys.argv[1], 'r')
    data = string_file.readlines()
    string_list = data[1].split(' ')
    # print 'string_list: %s' % string_list
    string = string_list[0]
    kmer_length = int(string_list[1])
    mismatches = int(string_list[2])

    mismatch_plus_one = mismatches # + 1

    # List of all kmers that have been compared.
    alphabet = ''.join(OrderedDict.fromkeys(string).keys())
    perms = [''.join(i) for i in product(alphabet,repeat=mismatches)]

    # print 'perms: %s' % perms

    # s = set()
    count_dict = {}
    compared_strings = []
    compared_list_list = []
    count = 0
    for i in range(0, len(string) - kmer_length):
        substring = string[i:(i + kmer_length)]

        if substring not in compared_strings:
            compared_strings.append(substring)
            # Now iterate over all the sets in the set list and see if the mismatch
            # count 
            for compared_list in compared_list_list:
                in_list = True
                for substr in compared_list:
                    if mismatch_count(substring, substr) > mismatch_plus_one:
                        in_list = False

                if in_list:
                    compared_list.append(substring)

            new_list = []
            new_list.append(substring)
            compared_list_list.append(new_list)

            # print 'compared_set_list: %s' % compared_set_list
            count = count + 1


    # print compared_list
    # print compared_list_list
    # print '\n'

    pruned_compared_list_list = []

    for compared_list in compared_list_list:
        if len(compared_list) > 1:
            pruned_compared_list_list.append(compared_list)

    for l in pruned_compared_list_list:
        # Pick the first two items in the list because:
        # 1. All lists of length == 1 have been removed
        # 2. All strings in the list mismatch on the same indicies.
        indices = mismatch_indices(l[0], l[1])

        # Turn the string into a list so that you can modify individual characters
        string_l = list(l[0])
        for perm in perms:
            count = 0
            for index in indices:
                string_l[index] = perm[count]
                count = count + 1

        string = "".join(string_l)

        if string in count_dict:
            count_dict[string] = count_dict[string] + 1
        else:
            count_dict[string] = 1

        # for substring in s:

    print 'count_dict: %s' % count_dict

    # print pruned_compared_list_list

    # in_common = kmer_length - mismatches

    # print 'string: %s, kmer_length: %s, mismatches: %s' % (string, kmer_length, mismatches)
    # # Also could have been the following, but would not have guarneeted the order.
    # # Since this is a smaller data set, I can sacrifice the performance for reproduceability.
    # # ''.join(set(string))
    # alphabet = ''.join(OrderedDict.fromkeys(string).keys())
    # perms = [''.join(i) for i in product(alphabet,repeat=kmer_length)]
    
    # # words = {}
    # words = []

    # max_count = 0

    # for perm in perms:
    #     total_mismatch = 0

    #     for i in range(0, len(string) - kmer_length):
    #         substring = string[i:(i+kmer_length)]

    #         if chars_in_common(perm, substring) >= in_common:
    #             total_mismatch = total_mismatch + 1

    #     if total_mismatch > max_count:
    #         max_count = total_mismatch
    #         words = [perm, ]
    #     elif total_mismatch == max_count:
    #         words.append(perm)

    # result = ' '.join(words)
    # print result

    # try:
    #     output_file = sys.argv[3]
    #     output = open(output_file, 'w')
    #     output.write(result)
    #     output.close()
    # except:
    #     pass

if __name__ == "__main__":
    main()