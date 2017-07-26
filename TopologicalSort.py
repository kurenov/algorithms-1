###
    # Code by Olzhas Kurenov
    # Implementation of Topological Sort Algorithm
    # Running time: O(n+m)
###
print '\n~~~~~~~~~Topological Sort Algorithm algorithm~~~~~~~~~\n'

graph = {};

with open('acyclicGraph.txt') as f:
    lines = f.readlines();

for line in lines:
    numbers = [int(x) for x in line.split()];
    graph[numbers[0] - 1] = {
        'visited': False,
        'label': -1,
        'edges': map(lambda v: v-1, numbers[1 : len(numbers)])
    };

n = len(lines);
currentLabel = n - 1;
print 'currentLabel', currentLabel;
print graph;

def DepthFirstSearch(g, s):
    global currentLabel;
    g[s]['visited'] = True;
    for edge in g[s]['edges']:
        if not g[edge]['visited']:
            DepthFirstSearch(g, edge);
    g[s]['label'] = currentLabel;
    currentLabel = currentLabel - 1;

def TopologicalSort(g):
    for edge in g:
        if not g[edge]['visited']:
            DepthFirstSearch(g, edge);

TopologicalSort(graph);

print graph;
