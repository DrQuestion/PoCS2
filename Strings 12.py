def capitalize(string):
    l=list(string)
    l[0]=l[0].upper()
    for i in range(1,len(l)):
        if l[i-1]== ' ':
            l[i]=l[i].upper()
    string=''.join(l)
    return string