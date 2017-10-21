from itertools import permutations
if __name__=='__main__':
    s=raw_input().split()
    l=sorted(list(permutations(s[0],int(s[1]))))
    for i in l:
        print ''.join(i)