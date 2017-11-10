from math import ceil

## Given a number of items, and the capacity for a box, determines
## the minimum number of boxes which will fit all items.
## If a box will be partially filled, this program
## will notify the user of this case.
print "Colfax Industries Shipping Boxes Calculator"

# Request information about the problem from the user.
numitems = input("Items quantitiy: ")
perbox = input("Quantity per box: ")

# Divide the number of items by the number of items per box.
# Convert 'perbox' to a float so we get floating point divison.
#   For example 50 items / 30.0 per box = 1.66 boxes.
# Then take the ceiling function of that to make sure we have enough
# boxes, and convert back to an integer for clean output.
numboxes = int(ceil(numitems/float(perbox)))
print "Required number of boxes: ", numboxes

# A box is partially filled if the number of items
# is not evenly divisble by the number per box.
print "Partially filled box: ",
if (numitems % perbox) == 0:
    print "No"
else:
    print "Yes"
