l=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([name, score])
l.sort(key=lambda x:x[1]) #here the lists are sorted with respect to grade, which is the element in position 1 of the inner lists
for i in l[1:]:
    if i[1]==l[0][1]:
        l.remove(i)
del l[0] # now only higher values are present
for i in l[1:]:
    if i[1]!=l[0][1]:
        l.remove (i) # now only 2nd lowest values are present
l.sort(key=lambda x:x[0]) #sort alphabetically
for e in l:
    print e[0] #names printed