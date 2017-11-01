def order_total(num):
    cost = 8.0 * num
    if num < 10:
        cost += 2.0 * num
    elif num < 25:
        cost += 40.0
    else:
        cost += 35.0

    return cost

num_hats = input("How many hats? ")
print "Your order total is $", order_total(num_hats)
