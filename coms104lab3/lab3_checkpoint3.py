from sample_functions import sing_verse
from sample_functions import longest


verse = input("Which verse would you like to sing (1-99)? ")
if verse < 0 or verse > 99:
    print "You're not very good at following directions! ;)"
else:
    sing_verse(verse)

first = raw_input("Enter the first string... ")
second = raw_input("Enter the second string... ")

print "The longer string is: ", longest(first, second)
