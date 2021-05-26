"""An exercise in computing the factorial of an int."""

__author__ = "730399808"


Number: int = int(input("Choose a number: "))

Factorial = 1
while Number > 0:
    Factorial = Factorial * Number
    Number = Number - 1

print("Factorial: " + str(Factorial))