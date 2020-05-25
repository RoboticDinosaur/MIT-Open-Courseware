# def main():
#     annual_salary = int(input('Enter your annual salary: '))
#     portion_save_percent = float(input('Enter the percent of your salary to save, as a decimal: '))
#     total_cost = int(input('Enter the cost of your dream home: '))
#     semi_annual_raise = float(input('Enter your semi annual raise: '))
#     portion_down_payment = total_cost * 0.25
#     savings = 0
#     r = float(0.04)
#     month = int(0)
#     while savings < portion_down_payment:
#         if month % 6 == 0 and month != 0:
#             annual_salary += annual_salary * semi_annual_raise
#         monthly_salary = annual_salary / 12
#         portion_saved = monthly_salary * portion_save_percent
#         roi = float(savings * r / 12)
#         savings += roi + portion_saved
#         month += 1
#     print('Number of months: ', month)

# Enter the starting salary: 150000
# Best savings rate: 0.4411
# Steps in bisection search: 12

# class Foo(object):
#     def __init__(self, initial_value):
#         self.value  = initial_value

# # Case 1
# a = Foo(45)
# print(a.value) # 45

# b = a

# print(b.value) # 45

# b.value = 100 
# print(b.value) # 100
# print(a.value) # 100

# # Case 2
# a = 45
# print(a) # 45
# b = a
# print(b) # 45

# b = 100 # different from b.value=100
# print(b) # 100
# print(a) # 45

# # Case 3
# a = Foo(45)
# print(a.value) # 45

# b = a

# print(b.value) # 45

# b = Foo(100)
# print(b.value) # 100
# print(a.value) # 45  <<<<<

# def hi(b):
#     b.value = 100
#     print(b.value)

# a = Foo(45)
# hi(a) # 100
# print(a.value) # 100

def calculate_savings(annual_salary, semi_annual_raise, annual_return, rate):
    savings = 0
    for month in range(36):
        # print('guess:%d month:%d savings_total:%f' % (num_guesses, month, savings))
        if month % 6 == 0 and month > 0:
            annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

        portion_saved = monthly_salary * rate
        roi = savings * annual_return / 12

        savings += roi + portion_saved
        month += 1

    return savings

def main():
    annual_salary = int(input('Enter your annual salary: '))
    total_cost = 1000000
    portion_down_payment = total_cost * .25
    semi_annual_raise = 0.07
    annual_return = 0.04
    savings = 0

    low = 0
    high = 10000
    guess = (high + low) // 2.0
    num_guesses = 0

    while abs(savings - portion_down_payment) >= 100:
        guess_rate = guess / 10000
            
        savings = calculate_savings(annual_salary, semi_annual_raise, annual_return, guess_rate)

        if savings < portion_down_payment:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2.0
        num_guesses += 1

        if num_guesses > 13:
            print("Can not calculate")
            break

    print('Steps: ', num_guesses)
    print('Best savings', guess)


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