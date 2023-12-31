print("hello, world")

input("What's your name? ")
print("My name is " + input())

name = input("What's your name? ")
print("My name is " + name)

name = input("What's your name? ")
print("My name is", name)

name = input("What's your name? ")
print("My name is ", end="")
print(name)

name = input("What's your name? ")
print("My name is", name, sep="???")

name = input("What's your name? ")
print('hello, "Allen"')

name = input("What's your name? ")
print("hello, \"ALLEN\"")

name = input("What's your name? ")

# Removes unwanted spaces
name = name.strip()

print(f"hello, {name}")

name = input("What's your name? ")

# Removes unwanted spaces and capitalizes the first letter
name = name.strip().capitalize()

print(f"hello, {name}")

name = input ("What’s your name? ")

# Removes unwanted spaces and capitalizes the first letter of each word
name = name.strip().title()

print(f"hello, {name}")

name = input ("What’s your name? ").strip().title()
print(f"hello, {name}")

name = input ("What’s your name? ").strip().title()

# Splitting the full name into the first and last name respectively
first, last = name.split(" ")

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y

print(z)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x/y, 2)

print(z)

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y
