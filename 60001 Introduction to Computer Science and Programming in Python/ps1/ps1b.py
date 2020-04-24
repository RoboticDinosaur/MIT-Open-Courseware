"""
Annual salary:    120000
Percent save:     .05
Total cost:       500000
Number of months: 142
"""

####
# Get the inputs direct to variables.
#####
annual_salary = int(input('Enter your annual salary: '))
portion_save_percent = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter your semi annual raise: '))

portion_down_payment = total_cost * 0.25
savings = 0

r = float(0.04)

month = int(0)

while savings < portion_down_payment:
    if month % 6 == 0 and month != 0:
        annual_salary += annual_salary * semi_annual_raise

    monthly_salary = annual_salary / 12


    portion_saved = monthly_salary * portion_save_percent
    roi = float(savings * r / 12)

    savings += roi + portion_saved
    month += 1


print('Number of months: ', month)
