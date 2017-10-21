from collections import OrderedDict
if __name__=='__main__':
    n=int(raw_input())
    ordered_dictionary = OrderedDict()#initialized the ordered dict
    for i in xrange(n):
        temp=raw_input().split()
        k=' '.join(temp[:len(temp)-1]) #each element in our splitted input up to the price is joined by ' ' so to form a string, which will be our key for the dict
        if k not in ordered_dictionary:
            ordered_dictionary[k]=int(temp[-1]) #if key doesn't exist, it is initialized with the corresponding value
        else:
            ordered_dictionary[k]+=int(temp[-1]) #if it exists, we sum the price again so to have stored eventually the net price
    for e in ordered_dictionary:
        print e, ordered_dictionary[e] #use this notation because OrderedDict has no attribute item