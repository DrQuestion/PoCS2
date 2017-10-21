from collections import deque
if __name__=='__main__':
    t=int(raw_input()) #number of testcases
    for _ in xrange(t): #iterating over the test cases
        n=raw_input()
        l=map(int,(raw_input().split()))
        d=deque(l) #created a deque containing all the values of the test case analyzed
        for _ in xrange(len(d)): #iterating over the indexes of the elements of d, which will progressively reduce
            a=d.popleft() #extracted first and last element of d
            b=d.pop()
            if len(d)==0: #at one step from the end of the cycle, if everything didn't respect the if statement on the bottom, if the number of elements in d is even, we'll end up with 2 elements, that are removed by pops() above, meaning that we can pile cubes
                print 'Yes'
                break
            elif len(d)==1: #if instead the number is odd, we'll end up with one element,
                if max(a,b)<d[0]: # that if it's bigger than the other two,
                    print 'No' #we can't pile it
                    break #and break the cycle
                else:
                    print 'Yes' #otherwise we can, and after printing yes we break the cycle
                    break
            if max(a,b)<d[0] or max(a,b)<d[-1]: #the nucleus of the code: when the max between the two removed extremities is less than one of the two actual extremities,
                print 'No' #it means that we can't pile
                break
            #if none of the previous if statements is verified, everything is ok by far and the cycle begins again with the two new extremities