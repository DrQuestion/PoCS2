def minion_game(string):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    lenght=len(string)
    for k,v in enumerate(string):
        if v in vowels:
            kevsc += (lenght-k) #lenght - k is the number of all possible substrings that begin with letter v, from the letter itself to all the other possible substrings up to the end of the string, this for each letter in the string. if v is a vowel, the quantity is summed up to kevin counter, while if it is a consonant points go to stuart
        else:
            stusc += (lenght-k)
    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"