from random import randint

# Create a random number for the user to guess.
goal = randint(1, 10)
# Not the actual guess, make sure it's wrong
# so we can enter the loop.
guess = 0

print "Try to guess a number between 1 and 10"
while guess != goal:
    guess = input("What is your guess: ");
    if guess == goal:
        print "That's it!"
    elif guess < goal:
        print "Too low!"
    else:
        print "Too high!"


