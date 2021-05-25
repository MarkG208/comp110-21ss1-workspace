"""An exercise in remainders and boolean logic."""

__author__ = "730399808"


Integer: int = int(input("Enter an int: "))

if Integer % 2 != 0 and Integer % 7 != 0:
    print("CAROLINA")
if Integer % 2 == 0 and Integer % 7 == 0:
    print("TAR HEELS")
else:
    if Integer % 2 == 0:
        print("TAR")
    if Integer % 7 == 0:
        print("HEELS")



 
