"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730399808"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
Fortune_Cookie: int = int(randint(1, 4))

if Fortune_Cookie == 1:
    print("The road to success and glory is intimidating yet fulfilling at the end.")
else:
    if Fortune_Cookie == 2:
        print("Right in front of your eyes is the love of your life.")
    else:
        if Fortune_Cookie == 3:
            print("Waiting for you later, is a pleasant surprise.")
        else:
            if Fortune_Cookie == 4:
                print("Tomorrow will be a better day. And if not, there's another tomorrow to experience.")
            else:
                print("Happiness isn't something that is meant to be pursued but rather created.")

print("Now, go spread positive vibes!")