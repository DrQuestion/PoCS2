if __name__=='__main__':
    k=int(raw_input())
    arr=map(int, raw_input().split())
    myset = set(arr)
    print(((sum(myset)*k)-(sum(arr)))//(k-1)) #calculated the sum of all elms both in the set as all elms were repeated and in the list, the difference is the number of captain room*(k-1)