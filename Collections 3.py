from collections import namedtuple
if __name__=='__main__':
    n=int(raw_input())
    params=raw_input().split()
    l=[]
    indm,indi,indn,indc=params.index('MARKS'),params.index('ID'),params.index('NAME'),params.index('CLASS')#so that respective indexes are stored to beused later
    Values=namedtuple('Values', 'ID NAME CLASS MARKS')#initialized the namedtuple that will contain id name class and marks
    for i in xrange(n):
        a=raw_input().split()
        l.append(int(Values(a[indi],a[indn],a[indc],a[indm]).MARKS))#inserted all values at right places for each line of input and inserted the value stored in MARKS inside a list. at the end we have all marks inside l
    print "{0:.2f}".format(sum(l)/float(len(l))) #simple average formatted to 2 positions after dot