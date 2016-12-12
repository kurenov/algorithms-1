###
    # Code by Olzhas Kurenov
    # Implementation of Depth-First Search Algorithm
    # Running time: O(n + m)
###
from Stack import Stack

print '\n~~~~~~~~~Karger\'s Minumum Cut algorithm~~~~~~~~~\n'

graph = {}
stack = Stack();

with open('graph.txt') as f:
    lines = f.readlines();

for line in lines:
    numbers = [int(x) for x in line.split()]
    graph[numbers[0] - 1] = {
        'visited': False,
        'edges': map(lambda v: v-1, numbers[1 : len(numbers)]),
        'distance': -1
    }

print graph;
