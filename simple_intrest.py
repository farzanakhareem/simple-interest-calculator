# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.

    :param principal: The principal amount
    :param rate: The rate of interest (as a percentage)
    :param time: The time period (in years)
    :return: The calculated simple interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# User input
try:
    principal_amount = float(input("Enter the principal amount: "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    time_period = float(input("Enter the time period (in years): "))

    # Calculate simple interest
    interest = calculate_simple_interest(principal_amount, annual_rate, time_period)

    # Output the result
    print(f"The calculated simple interest is: {interest}")
except ValueError:
    print("Please enter valid numeric input.")
