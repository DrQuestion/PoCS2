def print_rangoli(size):
    alphabet= list('abcdefghijklmnopqrstuvwxyz')
    H=size*2-1
    W=H*2-1
    a=0
    for i in range(1,H,2):
        print ('-'.join(['{}']*i)).format(*alphabet[size-1:size-(a+2):-1]+alphabet[size-a:size]).center(W,'-')
        a+=1
    print ('-'.join(['{}']*H)).format(*alphabet[size-1::-1]+alphabet[1:size])
    a-=1
    for i in range(H-2,-1,-2):
        print ('-'.join(['{}']*i)).format(*alphabet[size-1:size-(a+2):-1]+alphabet[size-a:size]).center(W,'-')
        a-=1