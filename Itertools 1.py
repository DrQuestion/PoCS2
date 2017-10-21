from itertools import product
if __name__=='__main__':
    l=map(str, list(product(map(int, raw_input().split()),map(int, raw_input().split()))))
    print ' '.join(l)