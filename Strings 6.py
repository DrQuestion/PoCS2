if __name__ == '__main__':
    s = raw_input()
    l=list(s)
    print any (str.isalnum() for str in l) #these ones following 'any' are generators which return every time the result of the validation methods, and 'any' is used because one single occurrance is sufficient for our purposes
    print any (str.isalpha() for str in l)
    print any (str.isdigit() for str in l)
    print any (str.islower() for str in l)
    print any (str.isupper() for str in l)