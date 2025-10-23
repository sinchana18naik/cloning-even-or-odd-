# Even and Odd Counter Program

numbers = []
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

even = len([n for n in numbers if n % 2 == 0])
odd = len([n for n in numbers if n % 2 != 0])

print("\nEven numbers:", even)
print("Odd numbers:", odd)
