"""
File: problem1.py
Author: Michael Iacobelli
Date: 2024-02-23
Description: Given the temperature at which water begins to boil,
             determine atmospheric pressure. 
"""

# sets the constant variable for the heading
heading = 'Boiling Water'
# prints and f string with the heading in the middle and 25 '-' either side
print(f'{heading:-^50}')

# gets radius of sphere input from user and stores as varible
user_water_boiling_point = float(input('Input water boiling point: '))

# computes the atmospheric pressure from water boiling point and stores as variable
atmospheric_pressure = 5 * user_water_boiling_point - 400

# prints a f-string so that I don't have to concatanate 
# I learned this on my own outside the course
print(f'This is the atmospheric pressure of the water: {atmospheric_pressure}kPa')