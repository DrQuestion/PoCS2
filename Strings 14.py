from collections import OrderedDict #useful for eliminating duplicates and mantaining previous order
def merge_the_tools(string, k):
    for i in xrange(len(string)/k): #we have n/l slices
        s=string[i*k:(i+1)*k] #slices have len=k, so this are the indexes relative to each slice
        str=''.join(OrderedDict.fromkeys(s)) #every character is stored as key into the dictionary, with value None, respecting the order. Being it a dictionary, key will be stored only once. Moreover, OrderedDict preserves storage order. Then keys are assembled into a string.
        print str