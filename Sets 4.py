if __name__=='__main__':
    N=int(raw_input())
    s=set()
    for i in range(N):
        s.add(raw_input())
    print len(s)