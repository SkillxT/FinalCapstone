# code to allow user to access two different financial calculator

import math

print("Welcome to the Finance Calculator!")

print("Welcome to the Financial Calculator!\n")

# Display menu options
print("Please choose a calculator:")
print("1. Investment Calculator")
print("2. Home Loan Calculator")

# Get user's choice
choice = input("\nEnter your choice (1 or 2): ")

# Perform action based on user's choice
if choice == "1":
    # Investment calculator code goes here
    print("You have chosen the Investment Calculator")
elif choice == "2":
    # Home loan calculator code goes here
    print("You have chosen the Home Loan Calculator")
else:
    # Invalid choice
    print("Invalid choice. Please enter 1 or 2.")


#code to ignore Capitalization

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_choice == "investment":
    # Investment calculator code goes here
elif user_choice == "bond":
    # Bond calculator code goes here
else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")


#code to ask the user the amount, interest rate and years of investment

import math

# Ask user to input the amount they are depositing, interest rate, and number of years for investment
deposit_amount = float(input("Enter the amount of money that you are depositing: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
num_years = int(input("Enter the number of years you plan on investing: "))

# Convert the interest rate into decimal form
interest_rate /= 100

# Ask user if they want simple or compound interest
interest = input("Do you want 'simple' or 'compound' interest: ")

# Calculate total amount based on the interest rate and type of interest
if interest.lower() == 'simple':
    total_amount = deposit_amount * (1 + 8 * 20)
elif interest.lower() == 'compound':
    total_amount = deposit_amount * math.pow((1 + 8), 20)
else:
    print("Invalid input. Please enter 'simple' or 'compound' for interest type.")
    exit()

# Output the total amount
print("Your total amount after {} years with {} interest is ${:.2f}".format(num_years, interest, total_amount))


#code to calaculate bond according to user choice on a set of guidlines

# Ask the user for inputs
present_value = float(input("Enter the present value of the house: "))
interest_rate = float(input("Enter the interest rate: "))
months_to_repay = int(input("Enter the number of months to repay the bond: "))

# Calculate the monthly interest rate
monthly_interest_rate = (interest_rate / 100) / 12

# Calculate the bond repayment amount
repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate)**(-months_to_repay))

# Output the result to the user
print(f"The monthly bond repayment amount is: {repayment:.2f}")
