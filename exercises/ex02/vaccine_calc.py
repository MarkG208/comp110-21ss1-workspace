"""A vaccination calculator."""

__author__ = "730399808"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Population: str = input("What is the population count? ")
Doses_Administered: str = input("What is the number of doses adminstered? ")
Doses_Per_Day: str = input("What is the number of doses per day? ")
Target_Percent: str = input("What is the target percent vaccinated? ")
Population_int: int = int(Population)
Doses_Administered_int: int = int(Doses_Administered)
Doses_Per_Day_int: int = int(Doses_Per_Day)
Target_Percent_int: float = int(Target_Percent) / 100
current_percentage: float = (Doses_Administered_int) / (Population_int * 2)
Percentage_to_go: float = Target_Percent_int - current_percentage
Vaccines_needed: int = round(Percentage_to_go * Population_int * 2)
Days_to_go: int = round(Vaccines_needed / Doses_Per_Day_int)
Duration: timedelta = timedelta(Days_to_go)
Final_date: datetime = datetime.today() + Duration
print("Population: " + Population)
print("Doses administered: " + Doses_Administered)
print("Doses per day: " + Doses_Per_Day)
print("Target percent vaccinated: " + Target_Percent)
today: datetime = datetime.today()
print("We will reach " + str(Target_Percent) + "% vaccination in " + str(Days_to_go) + " days, which falls on" + Final_date.strftime(" %B %d, %Y."))
