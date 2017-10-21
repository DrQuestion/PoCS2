from itertools import combinations_with_replacement
if __name__=='__main__':
    s=raw_input().split()
    a=sorted(list(s[0]))
    l=list(combinations_with_replacement(a,int(s[1])))
    for i in l:
        print ''.join(i)