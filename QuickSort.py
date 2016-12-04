###
    # Code by Olzhas Kurenov
    # Implementation of Quick Sort
    # Running time: O(n)
###

from random import randint

print '\n~~~~~~~~~n-th order statistics~~~~~~~~~\n'

print 'Reading input file\n'
with open('quickSort.txt') as f:
    lines = f.readlines()

numbers = [];
for line in lines:
    numbers.append(int(line))

numberOfComparisons = 0

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def getPivot(start, end, random):
    return end-1;
    if random and start < end:
        return randint(start, end - 1)    
    return end - 1;

def partitionAroundPivot(a, start, end, p):
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
    return p;

def QuickSort(a, start, end):
    print a[start : end];
    if (abs(end - start) <= 1):
        return;
    global numberOfComparisons
    numberOfComparisons += (end - start - 1)
    pivot = getPivot(start, end, True);
    pivot = partitionAroundPivot(a, start, end, pivot);
    QuickSort(a, start, pivot);
    QuickSort(a, pivot + 1, end);

QuickSort(numbers, 0, len(numbers));
print numbers;
print 'numberOfComparisons',numberOfComparisons
