num1 = 42 # variable declaration, initialize interger
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuples
print(type(fruit)) # access value, prints data type "string"
print(pizza_toppings[1]) # access value prints list element "Sausage"
pizza_toppings.append('Mushrooms') # add value, adds string element "Mushrooms" to back of pizza_toppings list
print(person['name']) # access value, prints the value of the key "name" in the person dictionary
person['name'] = 'George' # change value, reassigns the name keys value to "George"
person['eye_color'] = 'blue' # adds a new key value pair of "eye_color" = "blue"
print(fruit[2]) # prints the 3 element in the "fruit" tuple "banana"

if num1 > 45: # conditional if statement
    print("It's greater") 
else: # conditional else statement
    print("It's lower")

if len(string) < 5: # conditional if statement, string method length
    print("It's a short word!") # print string
elif len(string) > 15: # conditional else if statment, string method length
    print("It's a long word!") # print string
else: # conditional else statement
    print("Just right!") # print string

for x in range(5): # for loop stop
    print(x) # print code
for x in range(2,5): # for loop start and stop
    print(x) # print code
for x in range(2,10,3): # for loop start, stop, and increment
    print(x) # print code
x = 0 # variable declaration, initialize interger
while(x < 5): # while loop, stop value
    print(x) # print code
    x += 1 # increment

pizza_toppings.pop() # pop method, remove element end of list, list
pizza_toppings.pop(1) # pop method, remove element at index 1, list

print(person) # prints person variable dictionary
person.pop('eye_color') # remove key value pair "eye_color" = "blue"
print(person) # prints person variable dictionary without "eye_color" key

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if statement, boolean
        continue # continue keyword
    print('After 1st if statement') # print code
    if topping == 'Olives': # conditional if statement
        break # break keyword

def print_hello_ten_times(): # function
    for num in range(10): # for loop stop
        print('Hello') # print code

print_hello_ten_times() # defining function

def print_hello_x_times(x): # defining function, parameter
    for num in range(x): # for loop stop
        print('Hello') # print code

print_hello_x_times(4) # calling function, argument

def print_hello_x_or_ten_times(x = 10): # defining function, parameter
    for num in range(x): # for loop stop
        print('Hi') # print code

print_hello_x_or_ten_times() # calling function
print_hello_x_or_ten_times(4) # calling function, argument


"""
Bonus section
"""

num3 = 72
print(num3)
# fruit[0] = 'cranberry' # can't be modified cause tuples are immutable
# print(person['favorite_team']) # can't print "favorite_team" value cause it doesn't exist inside the dictionary
# print(pizza_toppings[7]) # can't print the indexed element because it doesn't exist within the "pizza_toppings" list
#   print(boolean) # syntax error for improper indentation
# fruit.append('raspberry') # can't add value to tuples
# fruit.pop(1) # can't remove value from tuples