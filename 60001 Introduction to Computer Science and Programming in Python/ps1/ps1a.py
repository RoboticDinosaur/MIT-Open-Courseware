"""
Annual salary:    120000
Percent save:     .10
Total cost:       1000000
Number of months: 183
"""

####
# Get the inputs direct to variables.
#####
ANNUAL_SALARY = int(input('Enter your annual salary: '))
PORTION_SAVE_PERCENT = float(input('Enter the percent of your salary to save, as a decimal: '))
TOTAL_COST = int(input('Enter the cost of your dream home: '))

MONTHLY_SALARY = ANNUAL_SALARY / 12
PORTION_DOWN_PAYMENT = TOTAL_COST * 0.25
SAVINGS = 0

R = float(0.04)

MONTH_COUNT = int(0)

while SAVINGS < PORTION_DOWN_PAYMENT:
    PORTION_SAVED = MONTHLY_SALARY * PORTION_SAVE_PERCENT
    ROI = float(SAVINGS * R / 12)

    SAVINGS += ROI + PORTION_SAVED
    MONTH_COUNT += 1

print('Number of months: ', MONTH_COUNT)
