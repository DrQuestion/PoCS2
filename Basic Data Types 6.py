if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n): #so to comprehend all the student
        line = raw_input().split() #forms a list of all the single elements in a line of input
        name, scores = line[0], line[1:] #creating a string name with the name and a list scores with the grades of each student
        scores = map(float, scores) #making each score float
        student_marks[name] = scores #inserting into the dictionary names as keys and lists of scores as values
    query_name = raw_input() #assigning to query_name the last line of input
    a=sum(student_marks[query_name])/len(student_marks[query_name]) #accessed in the dictionary to the list corresponding to the key: query_name
    print("%.2f" % a) #so to print two decimals