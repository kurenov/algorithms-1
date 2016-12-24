###
    # Code by Olzhas Kurenov
    # Implementation of Breadth-First Search Algorithm
    # Running time: O(n + m)
###
from Queue import Queue

print '\n~~~~~~~~~Breadth-First Search algorithm~~~~~~~~~\n'

graph = {}

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

def BreadthFirstSearch(g, s):
    # initialize starting vertex
    g[s]['visited'] = True
    g[s]['distance'] = 0
    q = Queue();
    q.put(g[s])
    # loop while queue is not empty
    while not q.empty():
        v = q.get()
        # iterate through edges in v
        for edge in v['edges']:
            if not g[edge]['visited']:
                print edge
                g[edge]['visited'] = True;
                g[edge]['distance'] = v['distance'] + 1;
                q.put(g[edge]);

BreadthFirstSearch(graph, 0)
print 'graph', graph
