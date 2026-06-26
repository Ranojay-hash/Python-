
# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Taking input from the user
num = int(input("Enter a number: "))

original = num
sum_fact = 0

# Calculate the sum of factorials of digits
while num > 0:
    digit = num % 10
    sum_fact += factorial(digit)
    num //= 10

# Check whether the number is Peterson or not
if sum_fact == original:
    print(original, "is a Peterson Number.")
else:
    print(original, "is NOT a Peterson Number.")