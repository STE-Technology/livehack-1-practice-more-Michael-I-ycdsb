"""
File: problem2.py
Author: Michael Iacobelli
Date: 2024-02-23
Description: Given the ages of the youngest and middle children,
             determine the age of the oldest child?
"""

# sets the constant variable for the heading
heading = 'Next in Line'
# prints and f string with the heading in the middle and 25 '-' either side
print(f'{heading:-^50}')

# gets age of youngest child and middle child then stores as varibles
youngest_child_age = int(input('Input the youngest childs age: '))
middle_child_age = int(input('Input the middle childs age: '))

# computes the oldest childs age then stores as variable
oldest_child_age = middle_child_age + (middle_child_age - youngest_child_age)

# prints a f-string so that I don't have to concatanate 
# I learned this on my own outside the course
print(f'This is the oldest childs age: {oldest_child_age}')