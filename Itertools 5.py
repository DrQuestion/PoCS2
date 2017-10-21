from itertools import groupby
if __name__=='__main__':
    s=raw_input()
    g=[]
    l=[]
    for occurrance,group in groupby(s):
        g.append(list(group))
    for i,j in enumerate(g):
        l.append('('+str(len(j))+', '+j[0]+')')
    print ' '.join(l)