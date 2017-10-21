if __name__ == '__main__':
    nouseful= raw_input()
    ints=map(int,raw_input().split())
    A=set(map(int,raw_input().split()))
    B=set(map(int,raw_input().split()))
    happiness=0
    for e in ints:
        if e in A:
            happiness+=1
        if e in B:
            happiness-=1
    print happiness