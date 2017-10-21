if __name__=='__main__':
    unused=raw_input()
    a=set(map(int, raw_input().split()))
    unused=raw_input()
    b=set(map(int, raw_input().split()))
    print len(a^b)