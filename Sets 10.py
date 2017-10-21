if __name__=='__main__':
    notuseful = raw_input()
    s = set(map(int, raw_input().split()))
    n=int(raw_input())
    for i in xrange(n):
        cmd=raw_input().split()
        a=set(map(int, raw_input().split()))
        eval('s.'+cmd[0]+'(a)')
    print sum(s)