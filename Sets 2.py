if __name__ == '__main__':
    n = raw_input()
    set1= set(map(int, raw_input().split()))
    n=raw_input()
    set2=set(map(int, raw_input().split()))
    for i in sorted(list(set1^set2)):
        print i