#!/usr/bin/python
import sys

def main():
    input_file = open(sys.argv[1], 'r')
    input_data = input_file.readlines()[0]

    base_pairs = {'C':'G', 'G':'C', 'A':'T', 'T':'A'}
    result = ''

    for char in input_data:
        result = base_pairs[char] + result 

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