###
    # Code by Olzhas Kurenov
    # Implementation of Karger's Minumum Cut algorithm
    # Running time: O(n^2*m)
###

import math as math
#import random from randint
from random import randint
import copy as copy

print '\n~~~~~~~~~Karger\'s Minumum Cut algorithm~~~~~~~~~\n'

graph = {}

print 'Reading input file\n'
with open('kargerMinCut.txt') as f:
    for line in f:
        numbers = [int(x) for x in line.split()]
        graph[numbers[0] - 1] = map(lambda v: v - 1, numbers[1 : len(numbers)])

def merge(g, a, b):
    # update edges of g[b] to point to a
    for i, adjacentVertex in enumerate(g[b]):
        for j, vertex in enumerate(g[adjacentVertex]):
            if vertex == b:
                g[adjacentVertex][j] = a;
    g[a] = g[a] + g[b]
    # remove self-loops
    g[a] = filter(lambda v: v != a and v != b, g[a])
    # make merged g[b] empty
    g[b] = []

def minCut(g, mergedVertices):
    if len(g) - mergedVertices <= 2:
        return
    # choosing random vertex a
    a = randint(0, len(g) - 1)
    # choosing non-emtpty (not yet merged) vertex
    while not len(g[a]):
        if a >= len(g) - 1:
            a = 0;
        else:
            a = a + 1;
    # choosing random vertex b, which is connected to a
    b = randint(0, len(g[a]) - 1)
    while not len(g[g[a][b]]):
        b =+ 1
        if b >= len(g[a]):
            b = 0
        if g[a][b] == a:
            b =+ 1
    merge(g, a, g[a][b])
    minCut(g, mergedVertices + 1)

vertices = len(graph)
minNumOfCuts = vertices
numberOfIterations = int(5 * math.ceil(math.log(vertices)))
for i in range(0, numberOfIterations):
    g = copy.deepcopy(graph);
    minCut(g, 1);
    localNumOfCuts = len(g);
    for v in g:
        if len(g[v]) and len(g[v]) < localNumOfCuts:
            localNumOfCuts = len(g[v]);
    print 'local min number of cuts', localNumOfCuts
    if localNumOfCuts < minNumOfCuts:
        minNumOfCuts = localNumOfCuts;

print 'min number of cuts', minNumOfCuts
