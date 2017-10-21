from collections import Counter
if __name__=='__main__':
    notused=raw_input()
    c=Counter(raw_input().split()) #dictionary where keys are shoes size and values are how many pairs are still present in store
    clients=int(raw_input())
    earned=0 #initialized the earned sum
    for _ in xrange(clients):
        client=raw_input().split() #every time a new client is taken from the input
        if client[0] in c: #if size is present a priori it enters the if statement, otherwise it continues with next client
            if c[client[0]]!=0: #if size is still present in store enters if statement, otherwise it continues with next client
                earned+=int(client[1]) #adds to earned sum the new income
                c[client[0]]-=1 #subtracts one pair of that size from the store
    print earned