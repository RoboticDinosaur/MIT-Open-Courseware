# https://stackoverflow.com/a/53375757/2579159
#
# https://github.com/angelichorsey/mit-eecs/blob/master/course_6_0001/problem-sets/ps1/ps1c.py
#
#
# I was close but I couldn't get my head around having so many points of information to help
# point me in the right direction.  This will only come with practice with real world problems.
# So I used some help from Stack Overflow to break my while loop down in to two seperate
# sections but this didn't make sense to me so I looked over the MIT solution and kept it as
# close to my original idea as possible.


def main():
    annual_salary = int(input('Enter your annual salary: '))

    semi_annual_raise = 0.07
    annual_return = 0.04
    total_cost = 1000000
    portion_down_payment = total_cost * 0.25
    monthly_salary = annual_salary / 12

    savings = 0

    num_guesses = 0
    low = 0
    high = 10000
    guess = (low + high) // 2.0


    while abs(savings - portion_down_payment) >= 100:
        savings = 0
        rate = guess / 10000

        temp_annual_salary = annual_salary

        for month in range(36):
            if month % 6 == 0 and month != 0:
                temp_annual_salary += temp_annual_salary * semi_annual_raise

            monthly_salary = temp_annual_salary / 12

            # portion_saved = monthly_salary * guess
            # roi = (savings * annual_return) / 12

            # savings += roi + portion_saved
            savings += monthly_salary * rate + savings * annual_return / 12

        if savings < portion_down_payment:
            # Look only in upper half search space
            low = guess
        else:
            # Look only in lower half search space
            high = guess

        # Next guess is halfway in search space
        guess = (low + high) / 2
        num_guesses += 1

        if num_guesses > 13:
            break

    print("Best saving rate:", guess)
    print("With current savings:", num_guesses)

main()