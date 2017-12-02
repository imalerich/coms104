def nFactorial(n):
    # 0! := 1
    if n == 0:
        print 1
        return

    result = 1
    for i in range(1, n+1):
        result *= i
    print result

# some test cases
nFactorial(0) # = 1
nFactorial(1) # = 1
nFactorial(2) # = 2
nFactorial(3) # = 6
nFactorial(4) # = 24
