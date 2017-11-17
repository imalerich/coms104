def findUserName(w):
    components = w.split()
    if len(components) != 3:
        print "ERROR - invalid input"
        return

    first = components[0].lower()
    last = components[1].upper()
    year = int(components[2])
    num = year + len(first)

    username = first + last + str(num)
    print username

findUserName("MARY   TWEED   1992")
findUserName("Ian Malerich 1995")
findUserName("United States_of_America 1776")
