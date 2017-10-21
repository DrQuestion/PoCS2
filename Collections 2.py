from __future__ import print_function
from collections import defaultdict
if __name__=='__main__':
    n,m=map(int,raw_input().split())
    d=defaultdict(list) #initialized the defdict which will contain each occurring element with its indexes
    a=[]
    b=[]
    for _ in xrange(n):
        a.append(raw_input()) #collected all elems of group a
    for _ in xrange(m):
        b.append(raw_input()) #collected all elems of group b
    for k,v in enumerate(a):
        d[v].append(k+1) #for each element of group a is initialized a key=the element in which we store the indexes of its occurrances
    for e in b:
        if e not in a:
            print (-1) #whenever an element in b is not in a, -1 is printed and the cycle continues
        else:
            print (*d[e]) #when instead it is present the whole indexes of occurance (*) are printed together