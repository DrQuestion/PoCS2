if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    p=2
    while arr[-p]==arr[-1]: #start from -2 because now -1 is for sure the largest, then while they are equal it proceeds back up to the 2nd largest number
        p+=1
    else: print arr[-p]