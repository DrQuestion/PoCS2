from collections import deque
if __name__=='__main__':
    d=deque() #initialized deque
    n=int(raw_input())
    for _ in xrange(n):
        cmd=raw_input().split()
        if len(cmd)>1: #if the cmd contains an object
            eval('d.'+cmd[0]+'('+cmd[1]+')') #evaluated the cmd with its object
        else:
            eval('d.'+cmd[0]+'()') #if the cmd doesn't contain any object
    print ' '.join(map(str, list(d))) #to print all the content of d in one string as requested