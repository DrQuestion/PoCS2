if __name__ == '__main__':
    n = int(raw_input()) #first input is the integer
    integer_list = map(int, raw_input().split()) #this splits the second input into a list of strings that are converted in turn into integers due to map function
    print (hash(tuple(integer_list))) #here list is converted into a tuple whose hash is calculated and printed