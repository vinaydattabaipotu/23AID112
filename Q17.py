import random
numbers = [random.randint(1, 100) for _ in range(8)]
print("List:", numbers)
biggest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
    if num < smallest:
        smallest = num
print("Biggest number:", biggest)
print("Smallest number:", smallest)
