N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2):
    print ('.|.'*i).center(M,'-') #don't need .l or .rjust because range is 1, 3 etc, so the right number of .|. is printed
print 'WELCOME'.center(M,'-')     #and just needs to be centered, surrounded by '-' so to acquire in each line len=M
for i in xrange(N-2,-1,-2):
    print ('.|.'*i).center(M,'-')