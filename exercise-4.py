# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

side_a = input('Enter the lengths of side a:')
side_b = input('Enter the lengths of side b:')
side_c = input('Enter the lengths of side c:')
if side_a == side_b and side_a == side_c:
    print(f'The triangle is equilateral - all three sides are equal in length')
elif side_a == side_b or side_c == side_a or side_c == side_b:
    print(f'The triangle is isosceles - two sides are the same length')
else:
    print(f'The triangle is scalene - all three sides are unequal in length')