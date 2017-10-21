if __name__=='__main__':
    notuseful = raw_input()
    s = set(map(int, raw_input().split()))
    n=int(raw_input())
    for i in xrange(n):
        cmd=raw_input().split()
        if len(cmd)>1:
            eval('s.'+cmd[0]+'('+cmd[1]+')')
        else: eval('s.'+cmd[0]+'()')
    print sum(s)