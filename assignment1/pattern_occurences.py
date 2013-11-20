#!/usr/bin/python
import sys

def main():
    string_file = open(sys.argv[1], 'r')
    strings = string_file.readlines()
    pattern = strings[0].rstrip()
    string = strings[1].rstrip()

    pattern_length = len(pattern)

    result = ''

    for i in range(len(string)):
        substring = string[i:(i+pattern_length)]

        if substring == pattern:
            if len(result) > 0:
                result = '%s %s' % (result, i)
            else:
                result = '%s' % i

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
