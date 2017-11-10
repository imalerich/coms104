from random import choice

## Perform a single game of Rock-Paper-Scissors
## Each player will press enter to accept, then a random
## move will be generated for that player.
## Each move is printed to the screen, then the winning player
## is determined and displayed.
print "Scissors-Rock-Paper (SRP) Game"

# Given an integer representing the player num,
# asks for the user confirmation, chooses a random move
# for that player, then prints and returns that move.
def read_player(num):
    options = ["Scissors", "Paper", "Rock"]
    raw_input("Player " + str(num) + ": Press ENTER to display a hand...")
    hand = choice(options)
    print hand
    return hand

# Get moves for each player.
player1 = read_player(1)
player2 = read_player(2)

# winning cases for player 1
if      ((player1 == "Scissors" and player2 == "Paper") or
        (player1 == "Paper"     and player2 == "Rock") or
        (player1 == "Rock"      and player2 == "Scissors")):
    print "Player1 wins"

# exact same cases, but rolls flipped, losing state for player 1
elif ((player2 == "Scissors" and player1 == "Paper") or
        (player2 == "Paper"     and player1 == "Rock") or
        (player2 == "Rock"      and player1 == "Scissors")):
    print "Player2 wins"

# nobody wins, the game is a draw
else:
    print "Game draws"

