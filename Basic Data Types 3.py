if __name__ == '__main__':
    x = int(raw_input()) #---v
    y = int(raw_input()) #----> the 3 dimensions
    z = int(raw_input()) #---^
    n = int(raw_input()) # the sum of the three coordinates can't be equal to this value
    print [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n] # 3 loops because we are moving into 3 dimension to get the coordinates