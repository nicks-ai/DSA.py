#variable assigment
num1 = 8
num2 = 7
result = num1 + num2
print(result)

name = "Nick"
print("Hello " + name)


#arithmetic operators
def calculate(num1, num2):
  sum = num1 + num2
  difference = num1 - num2
  product = num1 * num2
  if num2 == 0:
    qoutient = "cannot divide by zero"
  else:
    qoutient = num1 // num2
  return sum, difference, product, qoutient


num1 = 8
num2 = 7
print(calculate(5, 2))

base = 8
height = 6
area = 0.5 * base * height
print(area)
#comaprison operators
num1 = 8
num2 = 6
if num1 > num2:
  print("num1 is greater than num2")
else:
  print("num2 is greater than num1")
if num1 == num2:
  print("num1 is equal to num2")

str1 = "nick"
str2 = "nick"
if str1 == str2:
  print("they are same")
else:
   print("they are not the same")


#in and not in operators
fruits = ["apple", "cherry", "banana"]
if "apple" in fruits:
  print("apple is in the list of fruits")
else:
  print("apple is not IN in list of fruits")

sentence = "Hello, how are you?"
if "Hello" not in sentence:
  print("the word hello is not in in the sentence")
else:
  print("the word hello is in the sentence")
#list and list maipulation
my_list = []
my_list.append(5)
my_list.append(10)
my_list.append(15)
print(my_list)

numbers =[1, 2, 3, 4, 5]
numbers.pop()
print(numbers)

#sublist using slices
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublist = numbers[2:7]
print(sublist)

sentence = "Nick is real quick"
modified_sentence = sentence.replace("quick", "").strip()
print(modified_sentence)

#getting the index
colors = ["red", "blue", "violet", "green", "yellow"]
color_to_find = "green"
try:
    index = colors.index(color_to_find)
    print(f"The index of '{color_to_find}' is {index}.")
except ValueError:
     print(f"Color '{color_to_find}' not found in the list.")

fruits = ["grapes", "mango", "apple"]
fruits_to_find = "mango"
try: 
   index = fruits.index(fruits_to_find)
   print(f"index of '{fruits_to_find}'in {index}")
except ValueError:
   print(f"fruits '{fruits_to_find}' not found in the list")

#tuple
coordinates = (40.7128, -74.0060)
try:
    coordinates[0] = 34.0522
except TypeError as e:
    print(f"Error: {e}")

def quotient_and_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")
    
    quotient = dividend // divisor 
    remainder = dividend % divisor  
    
    return (quotient, remainder)

dividend = 10
divisor = 3
result = quotient_and_remainder(dividend, divisor)
print(f"The quotient and remainder of {dividend} divided by {divisor} are: {result}")

#dictionaries
person = {
    "first_name": 'nicklee',
    'last_name': 'almaida',
    'age': 20
}
person['city'] = "los angeles"

print(person)
#range()Function
numbers = range(1, 11)
for x in numbers:
   print(x)

even_numbers = list(range(2, 20, 2))

print(even_numbers)

#print()Funtion
print("hello, world")

fruits = ['apple', 'mango', 'grapes']
print(fruits)

#input()function
user_input = input("Please enter your name?")
print(f"Mr./Mrs {user_input}!")
#task2
num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a number:"))

product = num1 * num2

print(f"the product of num1 and num2 is, {product}!")


#len()function
favorite_books = [
    "The Hobbit by J.R.R. Tolkien",
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "The Catcher in the Rye by J.D. Salinger",
    "Pride and Prejudice by Jane Austen"
]

number_of_books = len(favorite_books)
print(f"There are {number_of_books} books in the list.")

# task2
user_sentence = input("Enter a sentence: ")
num_characters = len(user_sentence)
print(f"The number of characters in your sentence is {num_characters}.")

#continue/break statement
for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number)
#task2
for number in range(1, 21):
    if number == 15:
        break
    if number % 2 != 0:
        continue
    print(number)

#while and for loops
number = 1
while number <= 10:
   print(number)
   number += 1
#task2
names = ['Alice', 'Gou', 'nick', 'john']
for name in names:
   print(f'Hello, {name}!')

#writing functions
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print(f'The sum of 5 and 7 is: {result}')
#task2
def find_max(numbers):
    max_value = numbers[0]
    
    for number in numbers:
        if number > max_value:
            max_value = number
    
    return max_value

numbers_list = [3, 7, 1, 9, 5, 12, 8]
max_value = find_max(numbers_list)

print(f'The maximum value in the list is: {max_value}')

