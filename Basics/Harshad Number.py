# Taking input from the user
num = int(input("Enter a number: "))

original = num
sum_of_digits = 0

# Calculate the sum of digits
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

# Check if the number is divisible by the sum of its digits
if original % sum_of_digits == 0:
    print(original, "is a Harshad Number.")
else:
    print(original, "is NOT a Harshad Number.")