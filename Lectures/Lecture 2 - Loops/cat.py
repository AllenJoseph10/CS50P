print("Meow")
print("Meow")
print("Meow")

#i = 3
#while i!= 0:
#   print("Meow")

i = 3
while i != 0:
    print("Meow")
    i = i - 1

i = 1
while i <= 3:
    print("Meow")
    i = i + 1

i = 0
while i < 3:
    print("Meow")
    i += 1

# for loop

for i in [0,1,2]:
    print("Meow")

for i in range(3):
    print("Meow")

for _ in range(3):
    print("Meow")

#Result is meowmeowmeow
print("meow" * 3)

#Used to break a line between each meow
print("meow\n" * 3, end = "")

#while loop
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
      
for _ in range(n):
    print("meow")

# defining functions + for loop
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
