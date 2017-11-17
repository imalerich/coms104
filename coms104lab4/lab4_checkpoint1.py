def switcheroo(w, i, j):
    if i < 0 or j < 0 or i >= len(w) or j >= len(w) or i > j:
        print "ERROR - invalid indecies given."
        return

    sub1 = w[0:i]
    chari = w[i]
    sub2 = w[i+1:j]
    charj = w[j]
    sub3 = w[j+1:len(w)]

    res = sub1 + charj + sub2 + chari + sub3
    print res

switcheroo("Cs104", 1, 3) # C01s4
switcheroo("Cs104", 3, 1) # ERROR
switcheroo("blahXblahYblah", 4, 9) # blahYblahXblah
