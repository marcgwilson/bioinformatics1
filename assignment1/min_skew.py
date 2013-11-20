#!/usr/bin/python
import sys

def main():
    string_file = open(sys.argv[1], 'r')
    strings = string_file.readlines()
    string = strings[1].rstrip()

    total = 0
    minimum_value = 0
    indices = []

    for i in range(len(string)):
        char = string[i]

        if char is 'G':
            total = total + 1
        elif char is 'C':
            total = total - 1

        if total < minimum_value:
            # start a new list
            indices = [i + 1]
            minimum_value = total
        elif total == minimum_value:
            # add to list
            indices.append(i + 1)
        elif total > minimum_value:
            # do nothing in this case
            pass

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