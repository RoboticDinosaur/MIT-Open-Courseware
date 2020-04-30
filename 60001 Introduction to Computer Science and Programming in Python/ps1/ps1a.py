"""
Annual salary:    120000
Percent save:     .10
Total cost:       1000000
Number of months: 183
"""

####
# Get the inputs direct to variables.
#####
annual_salary = int(input('Enter your annual salary: '))
portion_save_percent = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

monthly_salary = annual_salary / 12
portion_down_payment = total_cost * 0.25
savings = 0

r = float(0.04)

month_count = int(0)

while savings < portion_down_payment:
    portion_saved = monthly_salary * portion_save_percent
    roi = float(savings * r / 12)

    savings += roi + portion_saved
    month_count += 1

print('Number of months: ', month_count)
