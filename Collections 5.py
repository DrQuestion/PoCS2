from collections import OrderedDict #had inspiration from previous code
if __name__=='__main__':
    n=int(raw_input())
    ordered_dictionary = OrderedDict() #initialized the ordered dict, this allows us to mantain order of occurrancy
    l=[] #this will eventually contain how many times each element has occurred
    for i in xrange(n):
        k=raw_input()
        if k not in ordered_dictionary: #initialized a new key whose value will be the counter of related word
            ordered_dictionary[k]=1
        else:
            ordered_dictionary[k]+=1 #if already present counter increases by one
    print len(ordered_dictionary)
    for k in ordered_dictionary:
        l.append(ordered_dictionary[k])
    print ' '.join(map(str,l)) #all the elements in l are print in one single string as requested by task