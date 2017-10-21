def count_substring(string, sub_string):
    counter=0 #so that even not finding anything returns 0
    l=[]
    for i in range(len(string)):
        l.append(string.find(sub_string,i)) #we progressively take note of the indeces where the subs is found
    l=list(set(l)) #eliminating duplicates
    l.remove(-1) #if we don't have found anything (or anything more) we don't want -1 to be counted as index
    return counter+len(l) #we count the indeces