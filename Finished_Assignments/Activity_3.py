import random

# Activity 3:

# Use forloops to solve the following problems.

# This function returns a random number between 1 and 100
# Usage: a = get_random_number()
# a would be a random number between 1 and 100


# 1. Create a list of 10 random numbers between 1 and 100. Hint: Remeber how you can append(add) to a list.
# Write your code below:

def get_random_number():
     return random.randint(1, 100)

a = []

for  i in range(10): 
    a.append(get_random_number())


# # # 2. Print the list of random numbers.
# # # Write your code below:

for i in range(len(a)):
     print(a[i])


# # # 3. Print the sum of the list of random numbers.
# # # Write your code below:

# a[0] # First item in list

# len(a) # Gives the length of the list

# for i in range(10) # Loops 10 times
#   # i goes from 0 - 9

total = 0

for i in range(len(a)):
    #  total = total + a[i]
    total += a[i]
    print(total)
     


# ---------------------------------------------------------

# We will create a simple while loop calculator tool similar to what we did in lecture.

# 1. First tell the user the commands they can use. The commands are: add, subtract, multiply, divide, exit

# 2. Ask the user to enter a command. If the user enters "exit", stop the while loop and print "Goodbye".

# 3. If the user enters "add", ask the user again for the first number, and then ask again for the second number. add them together and print the result.

# 4. If the user enters "subtract", ask the user again for the first number, and then ask again for the second number. subtract the second number from the first number and print the result.

# 5. If the user enters "multiply", ask the user again for the first number, and then ask again for the second number. multiply them together and print the result.

# 6. If the user enters "divide", ask the user again for the first number, and then ask again for the second number. divide the first number by the second number and print the result.

# Example 1:
# Enter a command: add
# Enter the first number: 5
# Enter the second number: 3
# The result is 8
# Enter a command: exit

# Example 2:
# Enter a command: divide
# Enter the first number: 10
# Enter the second number: 2
# The result is 5

# Write your code below:

a = 0
b = 0

command = input("Select one of the following commands: add, subtract, multiply, divide, or exit:")

print(command)

while command != "exit":
    if command == "add":
        a = input("Enter your first number:")
        b = input("Enter your second number:")
        print(int(a) + int(b))
        
    elif command == "subtract":  
        a = input("Enter your first number:")
        b = input("Enter your second number:")
        print(int(a) - int(b))
        
    elif command == "multiply":
        a = input("Enter your first number:")
        b = input("Enter your second number:")
        print(int(a) * int(b))
      
    elif command == "divide":
        a = input("Enter your first number:")
        b = input("Enter your second number:")
        print(int(a) / int(b))
     
    else:
        print("Command doesn't exist.")
    command = input("Enter a new command:")
    

