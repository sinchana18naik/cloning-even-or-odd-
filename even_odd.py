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
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime = len([n for n in numbers if is_prime(n)])
print("Prime numbers:", prime)