###
    # Code by Olzhas Kurenov
    # Implementation of Depth-First Search Algorithm
    # Running time: O(n + m)
###

print '\n~~~~~~~~~Depth-First Search algorithm~~~~~~~~~\n'

graph = {};

with open('graph.txt') as f:
    lines = f.readlines();

for line in lines:
    numbers = [int(x) for x in line.split()];
    graph[numbers[0] - 1] = {
        'visited': False,
        'edges': map(lambda v: v-1, numbers[1 : len(numbers)])
    };

print graph;

def DepthFirstSearch(g, s):
    print s;
    g[s]['visited'] = True;
    for edge in g[s]['edges']:
        if not g[edge]['visited']:
            DepthFirstSearch(g, edge);

DepthFirstSearch(graph, 0);
