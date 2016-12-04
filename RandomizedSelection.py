###
    # Code by Olzhas Kurenov
    # Implementation of n-th order statistics
    # Running time: O(n)
###

from random import randint

print '\n~~~~~~~~~n-th order statistics~~~~~~~~~\n'

print 'Reading input file\n'
with open('orderStatistics.txt') as f:
    lines = f.readlines()

numbers = [];
for line in lines:
    numbers.append(int(line));

def swap(a,i,j):
    print 'swapping',i,j,a[i],a[j]
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def getPivot(start, end, random):
    if random and start < end:
        return randint(start, end - 1)
    return end - 1;

def partitionAroundPivot(a, start, end, p):
    print 'Partitioning around Pivot'
    print start, end, p;
    print a[start: end];
    for i in range(start, end):
        print p, i;
        if (p == i):
            continue;
        if a[i] < a[p] and i > p:
            if (abs(i - p) == 1):
                swap(a,i,p);
                p=i;
            else:
                swap(a,i,p + 1);
                swap(a,p,p + 1);
                p+=1;
        elif a[i] > a[p] and i < p:
            swap(a,i,p);
            p=i;
        print a[start : end];
    return p;

def RSelect(a, start, end, order):
    print 'RSelect'
    print a[start : end];
    if (abs(end - start) <= 1):
        return;
    pivot = getPivot(start, end, True);
    print 'pivot', pivot
    pivot = partitionAroundPivot(a, start, end, pivot);
    if order==pivot:
        return;
    elif order < pivot:
        RSelect(a, start, pivot, order)
    else:
        RSelect(a, pivot + 1, end, order)

    print a[start : end];

RSelect(numbers, 0, len(numbers), 4);
