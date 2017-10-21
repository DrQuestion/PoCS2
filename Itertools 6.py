from itertools import combinations
if __name__=='__main__':
    N=int(raw_input())
    l=raw_input().split()
    K=int(raw_input())
    cmbs=list(combinations(range(N),K))#no need to calculate indeces as starting from 1
    inds=[]
    occurrancy_tuples=set()#to avoid redundancies using filter
    for k,v in enumerate(l):
        if v=='a':
            inds.append(k) #collecting indeces
    for ind in inds:
        occurrancy_tuples|=set(filter(lambda i: ind in i, cmbs)) #to cut all tuples not containing our index
    print "{0:.3}".format(len(occurrancy_tuples)/float(len(cmbs))) #formatting so to have precision to the third position