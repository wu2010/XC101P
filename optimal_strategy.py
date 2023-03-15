# a game for Alice and Bob. Assume that both of them take the optimal strategy.

# There are two piles of stones, each time a player can choose one pile of stones,
# and take away any number of stones from that pile.
# The person who takes the last stone wins.

# Alice always plays first, and we want to know who will be the winner.
# input: One line provides two numbers x, y, indicating the number of stones in the two piles
# The optimal strategy for Alice is to remove the extra stones in one pile such that two piles are equal.
# When two piles are equal, whoever goes first will lose
# because the second player will take the same amount from the other pile and eventually take the last stone.

x, y = map(int, input().split())

if x == y:
    # When two piles are equal, whoever goes first will lose
    print("Bob")
else:
    print("Alice")
