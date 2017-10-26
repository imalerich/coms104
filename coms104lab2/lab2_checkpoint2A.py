name = raw_input("Customer's full name: ")
nights = input("Number of nights: ")
room = input("Total room service charge($): ")
tele = input("Total telephone charge($): ")

totalRoomCharge = (55 * nights)
entertainmentTax = (totalRoomCharge * 0.1)
total = totalRoomCharge + room + tele + entertainmentTax

print "River Bend Hotel Bill (Customer : " + name + ")"
print "Total room charge($):", totalRoomCharge
print "Entertainment tak($):", entertainmentTax
print "Total bill($):", total
