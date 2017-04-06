###
    # Code by Olzhas Kurenov
    # Implementation of Recursive Breadth-First Search Algorithm
    # Running time: O(n + m)
###

print '\n~~~~~~~~~Breadth-First Search Algorithm~~~~~~~~~\n';
graph = {};

# reading input file
f = open('graph.txt', 'r');
for line in f.readlines():
    numbers = [ int(x)-1 for x in line.split() ];
    graph[numbers[0]] = {
        'visited': False,
        'distance': 0,
        'edges': numbers[1: len(numbers)]
    };
f.close();

print graph, "\n";

def breadthFirstSearch(g, v = 0):
    if g[v]['distance'] == 0:
        g[v]['visited'] = True;
    print "Edge", g[v];
    edges = [];
    #g[v]['distance'] = distance;
    for edge in g[v]['edges']:
        print edge;
        if not g[edge]['visited']:
            g[edge]['visited'] = True;
            g[edge]['distance'] = g[v]['distance'] + 1;
            edges.append(edge);
    for edge in edges:
        breadthFirstSearch(g, edge);

breadthFirstSearch(graph);

print "\n", graph;
