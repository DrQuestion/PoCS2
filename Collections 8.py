from collections import Counter #counter has a very useful object, which is most common, whose result allows us to print the content in the way we want, since it returns a list of tuples
if __name__ == "__main__":
    s = raw_input()
    c=Counter(s) #created counter of the string
    s=c.most_common(3) #list with three tuples containing elements most common and number of their occurrancies
    s.sort(key=lambda x: (-x[1], x[0])) #sorted in descending order of number, or ascending order of letter when the number is the same (had inspiration from our 5th lecture)
    for x,y in s:
        print x,y