from itertools import combinations
if __name__=='__main__':
    s=raw_input().split()
    a=sorted(list(s[0]))
    l=[]
    for i in xrange(1,int(s[1])+1):
        l+=list(combinations(a,i))
    for i in l:
        print ''.join(i)