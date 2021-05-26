"""Repeating a beat in a loop."""

__author__ = "730399808"


Beat_Repeated: str = str(input("What beat do you want to repeat? "))
Number_of_Repeats: int = int(input("How many times do you want to repeat it? "))
Result: str = ""

Repeat: int = 0
while Repeat < Number_of_Repeats:
    Result += Beat_Repeated + " "
    Repeat += 1
else:
  if Repeat <= 0:
    Result = ("No beat...")

print(Result)