####
# Get the inputs direct to variables.
#####
def main():
    annual_salary = int(input('Enter your annual salary: '))

    # portion_save_percent = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = 1000000
    semi_annual_raise = 0.07

    portion_down_payment = float(total_cost * 0.25)

    # Set savings to zero so we have something to start with
    savings = 0

    annual_return = 0.04
    #cube = 0.25
    #epsilon = 0.01

    # Initialise our starting values.
    num_guesses = 0
    low = 0
    high = 10000
    guess = (high + low) // 2.0

    # while we are not within our margin
    while abs(savings - portion_down_payment) >= 100:
        # reset our savings
        savings = 0

        # set our initial guess
        guess_rate = guess / 10000

        # make a copy of our annual salary
        temp_annual_salary = annual_salary

        # calculate the savings made within 3 years.
        for month in range(36):

            # Update our salary every 6 months
            if month % 6 == 0 and month != 0:
                temp_annual_salary += temp_annual_salary * semi_annual_raise

            # Update our monthly salary if needed
            monthly_salary = temp_annual_salary / 12

            # Set how much we saved this month with out new salary and our guess
            # interest rate.
            portion_saved = monthly_salary * guess_rate

            # Add on our ROI
            roi = float(savings * annual_return / 12)

            # Update our total savings
            savings += roi + portion_saved

            # Update the month count until the end and break out.
            month += 1


        # Check if our savings are less that our required down payment
        if savings < portion_down_payment:
            low = guess
        else:
            high = guess

        # next guess is halfway in search space
        guess = (high + low) / 2

        # update our guess count
        num_guesses += 1

        # Prevent our infinate loop as we can't make the count work.
        if num_guesses > 13:
            print("Could not calculate")
            break

    print('Best savings rate:', guess)
    print('Steps in bisection search:', num_guesses)

main()

#cube = 27
##cube = 8120601
## won't work with x < 1 because initial upper bound is less than ans
##cube = 0.25
#epsilon = 0.01
#num_guesses = 0
#low = 0
#high = cube
#guess = (high + low)/2.0
#while abs(guess**3 - cube) >= epsilon:
#    if guess**3 < cube:
#        # look only in upper half search space
#        low = guess
#    else:
#        # look only in lower half search space
#        high = guess
#    # next guess is halfway in search space
#    guess = (high + low)/2.0
#    num_guesses += 1
#print('num_guesses =', num_guesses)
#print(guess, 'is close to the cube root of', cube)