#!/usr/bin/python
import sys


# Returns a lits of kmers from the loaded data
def build_node_dict(data):
    nodes = {}
    for d in data:
        d = d.strip()
        if d == 'Output':
            break
        else:
            node_data = d.split(' -> ')

            s = int(node_data[0])
            ts = node_data[1].split(',')

            nodes[s] = map(int, ts)
    return nodes


def main():
    # The DNA(?) string to parse
    data_file = open(sys.argv[1], 'r')
    data = data_file.readlines()

    edges = build_node_dict(data[1:])

    edges_list = edges.items()

    key, value = edges_list[0]

    # If there's only one edge for this starting node, remove the key
    # Otherwise, just remove this particular edge
    if len(value) == 1:
        edges.pop(key)
    else:
        edges[key] = value[1:]

    path = [[key, value[0]]]

    index = 0
    while len(edges) is not 0:
        key = path[index][1] # The key we're looking for is the second element in list of length 2 that represents our edge.
        # Now find the next edge to add to our path

        if key in edges:
            value = edges[key]
            path.insert(int(index + 1), [int(key), int(value[0])])
            if len(value) == 1:
                edges.pop(key)
            else:
                edges[key] = value[1:]
            index+=1
        else:
            for i in range(len(path)):
                p = path[i]
                key = p[1] # Use the value as the key we're looking for
                if key in edges:
                    value = edges[key]
                    if len(value) == 1:
                        edges.pop(key)
                    else:
                        edges[key] = value[1:]
                    path.insert(i + 1, [key, value[0]])
                    index = i + 1


    # Give result an initial value, then iterate over the edges and append p[1]
    result = [str(path[0][0])]

    for p in path:
        result.append(str(p[1]))

    output = '->'.join(result)
    print output


if __name__ == "__main__":
    main()