
# Taking input from the user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
time = float(input("Enter Time (in years): "))
n = int(input("Enter Number of times interest is compounded per year: "))

# Compound Interest Formula
amount = principal * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principal

# Displaying the results
print("\n----- Result -----")
print(f"Principal Amount      : ₹{principal:.2f}")
print(f"Final Amount          : ₹{amount:.2f}")
print(f"Compound Interest     : ₹{compound_interest:.2f}")