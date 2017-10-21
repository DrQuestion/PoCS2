if __name__=='__main__':
    s=set(map(int, raw_input().split()))
    l=[]
    for i in xrange(int(raw_input())):
        l.append(s.issuperset(set(map(int, raw_input().split()))))
    print all(l)