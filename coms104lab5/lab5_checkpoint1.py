query = raw_input("Enter a phrase/sentence: ")
print "Indecies of a: "

for idx in range(len(query)):
    if query[idx].upper() == 'A':
        print query[idx], "at index", idx
