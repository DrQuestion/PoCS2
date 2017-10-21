from itertools import product
if __name__=='__main__':
    k,m= map(int,(raw_input().split()))
    l=[] #initialized the nested list which will contain all the k lists of elements
    moduli=[] #initialized the list which will contain the moduli at the end
    for _ in xrange(k):
        a=map(int,raw_input().split())
        del(a[0]) #we are not interested in the number of elements if we use map()
        l.append(a) #in l we append all the lists of elements
    for i in xrange(len(l)):
        l[i]=map(lambda x: x ** 2, l[i]) #here we square all the elements in the sublists of l (we apply the f of the task actually)
    prods=list(product(*l)) #here the cartesian products of all the elements (now the squares) accross the sublists of l are collected, so to have all possible lists of k elements that eventually we need to find the maximum modulus possible
    for i in xrange(len(prods)):
        prods[i]=sum(prods[i]) #here all sublists are converted into the sum of their elements (so into the S of the task actually)
    for s in prods:
        moduli.append(s%m) #now all the possible moduli are appended to the list
    print max(moduli) #printed the maximum modulus