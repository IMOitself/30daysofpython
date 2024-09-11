# day 2 at 10 pm
import math


first_name = ' miku '
last_name = ' hatsune '
full_name = first_name + last_name

is_japanese = True

if(is_japanese):
    full_name = last_name + first_name


funny_number = 69.0000069
str_funny_number = str(funny_number)
int_funny_number = int(funny_number)

print(full_name)
print(str(is_japanese))

print()
print(funny_number, type(funny_number))
print(str_funny_number)
print(int_funny_number)
print(str(int_funny_number))
print(float(int_funny_number))
print(list(str_funny_number))
print(len(first_name))

num_one = 5
num_two = 4

print()
print(num_one , num_two)
print('add', num_one + num_two)
print('sub', num_one - num_two)
print('multi', num_one * num_two)
print('div', num_one / num_two)
print('remainder', num_two % num_one)
print('power', num_one ** num_two)
print('round down', num_one // num_two)

radius = 30
print()
print('radius', radius)

area = math.pi * (radius ** 2)


print('area', area)

circum = 2 * (math.pi * radius)

print('circumference:', circum)

first_name = input('first name: ')

last_name = input('last name: ')

print()
print('input: ', first_name, last_name)