####
# Get the inputs direct to variables.
#####
def main():
    annual_salary = int(input('Enter your annual salary: '))

    # portion_save_percent = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = 1000000
    semi_annual_raise = 0.07

    portion_down_payment = float(total_cost * 0.25)
    savings = 0

    annual_return = 0.04
    #cube = 0.25
    #epsilon = 0.01
    num_guesses = 0
    low = 0
    high = 10000
    guess = (high + low) // 2.0

    while abs(savings - portion_down_payment) >= 100:
        savings = 0
        guess_rate = guess / 10000

        temp_annual_salary = annual_salary

        for month in range(36):
            if month % 6 == 0 and month != 0:
                temp_annual_salary += temp_annual_salary * semi_annual_raise

            monthly_salary = temp_annual_salary / 12

            portion_saved = monthly_salary * guess_rate
            roi = float(savings * annual_return / 12)
            savings += roi + portion_saved

            print('guess_rate:', guess_rate)
            print('month:', month)
            print('savings:', savings)
            
            month += 1

        if savings < portion_down_payment:
            low = guess
        else:
            high = guess

        # next guess is halfway in search space
        guess = (high + low) / 2
        num_guesses += 1

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