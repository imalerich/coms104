num = input("How many mousetraps? ")
res = raw_input("Are you an Iowa resident (y/n)? ")

if num <= 50:
    subtotal = num * 2.00
else:
    first = 50 * 2.00
    extra = (num - 50) * 1.50
    subtotal = first + extra

print "Subtotal:", subtotal

if res == "y":
    tax = subtotal * 0.05
else:
    tax = subtotal * 0.1

print "Tax:", tax
print "Total:", (subtotal + tax)
