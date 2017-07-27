###
    # Code by Olzhas Kurenov
    # Implementation of Straightforward Dijkstra's Shortest Path Algorithm
    # (without using a Heap)
    # Running time: O(n * m)
###
print '\n~~~~~~~~~Breadth-First Search algorithm~~~~~~~~~\n'

from Queue import Queue;

graph = {};
explored = [];
distances = {};

f = open('dijkstraData.txt', 'r');
for line in f.readlines():
    vertex = 0;
    for key, value in enumerate(line.split()):
        if key == 0:
            vertex = int(value);
            graph[vertex] = {
                'explored': False,
                'distance': None,
                'edges': {}
            };
        else:
            edge, distance = [int(x) for x in value.split(',')];
            graph[vertex]['edges'][edge] = distance;
f.close();

def depthFirstSearch(g, s = 0):
    for edge in g[s]['edges']:
        if not g[edge]['explored']:
            g[edge]['explored'] = True;
            depthFirstSearch(g, edge);

def breadthFirstSearch(g, s = 0):
    g[s]['explored'] = True;
    g[s]['distance'] = 0;
    q = Queue();
    q.put(s);
    while not q.empty():
        v = q.get();
        for edge in g[v]['edges']:
            if edge in g and not g[edge]['explored']:
                g[edge]['explored'] = True;
                g[edge]['distance'] = g[v]['distance'] + 1;
                q.put(edge);

def DijkstrasShortestPath(g, s = None):
    global distances, explored;
    if s >= 0:
        g[s]['explored'] = True;
        g[s]['distance'] = 0;
        distances[s] = 0;
        explored.append(s);
    v = None;
    w = None;
    minDist = 1000000;
    for e in explored:
        for d in g[e]['edges']:
            if not g[d]['explored']:
                dist = distances[e] + g[e]['edges'][d];
                #print e, w, dist
                if dist < minDist:
                    minDist = dist;
                    v = e;
                    w = d;
    print v, w, minDist
    if v > 0 and w > 0:
        g[w]['explored'] = True;
        g[w]['distance'] = 0;
        distances[w] = minDist;
        explored.append(w);
        DijkstrasShortestPath(g);

DijkstrasShortestPath(graph, 1);
print distances;

printDistances = [7,37,59,82,99,115,133,165,188,197];
result = "";

for pd in printDistances:
    result = result + str(distances[pd]) + ",";

print result;
