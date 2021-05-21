"""The numeric operator code calculates the entered values with multiple expressions."""

__author__: str = "730399808"

Left_hand_side: str = input("What is the left-hand side variable? ")
Right_hand_side: str = input("What is the right-hand variable? ")
Left_hand_side_int: int = int(Left_hand_side)
Right_hand_side_int: int = int(Right_hand_side)
print("Left-hand side" ": " + Left_hand_side)
print("Right-hand side" ": " + Right_hand_side)
Exponentiation: int = Left_hand_side_int ** Right_hand_side_int
print(str(Left_hand_side) + " ** " + str(Right_hand_side) + " is " + str(Exponentiation))
Division: float = Left_hand_side_int / Right_hand_side_int
print(str(Left_hand_side) + " / " + str(Right_hand_side) + " is " + str(Division))
Integer_Divison: int = Left_hand_side_int // Right_hand_side_int
print(str(Left_hand_side) + " // " + str(Right_hand_side) + " is " + str(Integer_Divison))
Remainder: int = Left_hand_side_int % Right_hand_side_int
print(str(Left_hand_side) + " % " + str(Right_hand_side) + " is " + str(Remainder))