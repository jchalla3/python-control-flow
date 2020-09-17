# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec):').lower()
day = int(input('Enter the day of the month:'))
if day >= 32:
    input('Please enter a day before the 32nd:')
else:
    if month in 'dec' and day >= 21 or month in 'jan' and day <= 31 or month in 'feb' or month in 'mar' and day <= 19:
        print(f'{month.capitalize()} {day} is in Winter')
    elif month in 'mar' and day >= 20 or month in 'apr may' or month in 'jun' and day <= 20:
        print(f'{month.capitalize()} {day} is in Spring')
    elif month in 'jun' and day >= 21 or month in 'jul aug' or month in 'sep' and day <= 21:
        print(f'{month.capitalize()} {day} is in Summer')
    elif month in 'sep' and day >= 22 or month in 'oct nov' or month in 'dec' and day <= 20:
        print(f'{month.capitalize()} {day} is in Fall')
    else:
        print('Error. Please try again.')