#!/usr/bin/python
import sys

def chars_in_common(first, second):
    count = 0

    if len(first) != len(second):
        return count

    for i in range(len(first)):
        if first[i] == second[i]:
            count = count + 1

    return count

def main():
    string_file = open(sys.argv[1], 'r')
    strings = string_file.readlines()
    pattern = strings[1].rstrip()
    string = strings[2].rstrip()
    mismatches = int(strings[3].rstrip())

    in_common = len(pattern) - mismatches

    indices = []

    for i in range(len(string)):
        substring = string[i:(i+len(pattern))]

        if chars_in_common(pattern, substring) >= in_common:
            indices.append(i)

    result = ' '.join(str(x) for x in indices)
    print result

    try:
        output_file = sys.argv[2]
        output = open(output_file, 'w')
        output.write(result)
        output.close()
    except:
        pass

if __name__ == "__main__":
    main()
