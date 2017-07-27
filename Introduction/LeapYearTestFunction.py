# Author: Pradeep K. Pant, ppant@cpan.org
# Write a function to test leap year
# We add a Leap Day on February 29, almost every four years. 
# The leap day is an extra, or intercalary, day and we add it to the shortest 
# month of the year, February. In the Gregorian calendar three criteria 
# must be taken into account to identify leap years:
# The year can be evenly divided by 4, unless;
# The year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 
# are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
def is_leap(year):
    leap = False
    #if year%4==0 and year%100!=0 or year%400==0:
    if year%4!=0: 
        leap = False      
    elif year%100!=0:
        leap = True
    elif year%400!=0: 
        leap = False
    else:
        leap = True
    # Write your logic here
    
    return leap
year = int(input())
print(is_leap(year))