# Task 1: Set up the environment by getting python ready to use
print("Task 1:")
print("Hello, I'm learning Python!\n")

# Task 2: Create variables with example data by storing information
# Personal Infromation (Example data - Safe to share)
first_name = "Alex"
last_name = "Johnson"
age = 28
email = "alex.johnson@example.com"
city = "Toronto"
country = "Canada\n"

# Task 3: Printing information by displaying it in a formatted way
print("Task 3:")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Location: {city}, {country}\n") 

# Task 4: Perform Calculations by using variables to do math
# 1. How old will Alex be in 10 years?
print("Task 4:")
new_age = 10 + age
print(f"Alex will be {new_age}years in 10 years.")

# 2. How old was Alex 5 years ago?
new_age2 = age - 5
print(f"Alex was {new_age2}years, 5 years ago.")

# 3. How many days has Alex been alive?
days_alive = age * 365
print(f"Alex has been alive for {days_alive} days.")

# 4. How many years until retirement at 65?
retire_age = 65 - age
print(f"Alex has {retire_age} years left until retirement.")

# Task 5
# Identifying data types
print(type(first_name))
print(type(age)) 
print(type(str(age)))
print(type(email))
print(type(days_alive))

# Operations
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print("Hello" + " " + "World")