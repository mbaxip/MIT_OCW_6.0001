"""

Part B: Saving, with a raise 

Background

In Part A, we unrealistically assumed that your salary didn’t change. 
But you are an MIT graduate, and clearly you are going to be worth more to your company over time! 
So we are going to build on your solution to Part A by factoring in a raise every six months.

In ​ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to 
include the following
1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage) 
2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h
month, the 18​th​ month, and so on.

Write a program to calculate how many months it will take you save up enough money for a down payment. 
Like before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment percentage 
is 0.25 (or 25%). 
Have the user enter the following variables:
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)

"""

# User Inputs

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# Initialize Variables

portion_down_payment = 0.25  # Portion of the cost needed for a down payment: 25%
cost_down_payment = portion_down_payment * total_cost

current_savings = 0

r = 0.04  # Invest current savings with annual rate of return, r: 4%

number_months = 0

# Calculate number of months needed to save enough money for a down payment

while current_savings < cost_down_payment:
    monthly_investment_return = current_savings * r/12

    monthly_salary_saved = portion_saved * annual_salary / 12

    current_savings = current_savings + monthly_investment_return + monthly_salary_saved
    number_months = number_months + 1

    if number_months > 0 and number_months % 6 == 0:
        annual_salary = annual_salary + semi_annual_raise * annual_salary

print('Number of months: ', number_months)
