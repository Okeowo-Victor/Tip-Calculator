print("Welcome to the Tip calculator !")
# Get the total bill amount from the user
bill_amount = float(input("Enter the total bill amount:$ "))

# Get the tip percentage from the user
tip_percentage = float(input("what tip percentage would you like to give (e.g, 15 for 15%): "))



# Calculate the tip amount
tip_amount = (tip_percentage / 100 * bill_amount)

# let Calculate the total amount (bill + tip)
total_amount = bill_amount + tip_amount

# Let now Print the results
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${total_amount:.2f}")


# # Note
# Why use :.2f?
# This is useful because when you're dealing with money (like a tip), you typically want to show two decimal places, regardless of whether the value is a whole number or not,
# The .2f formatting makes sure that the output is rounded and displayed in a consistent format (with exactly two decimal places).