# $1.26 can be broken down into 5 Quarters, and 1 Penny

amount = 126
quarters = amount / 25
amount = amount % 25
dimes = amount / 10
amount = amount % 10
nickels = amount / 5
amount = amount % 5
pennies = amount

print "Quarters: ", quarters
print "Dimes: ", dimes
print "Nickels: ", nickels
print "Pennies: ", pennies
