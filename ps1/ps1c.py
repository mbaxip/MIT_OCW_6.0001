"""
Part C: Finding the right amount to save away
​Please
In Part B, you had a chance to explore how both the percentage of your salary that you save each month and 
your annual raise affect how long it takes you to save for a down payment. 
This is nice, but suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years. 
How much should you save each month to achieve this? In this problem, you are going to write a program to answer that 
question. 
To simplify things, assume:
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)
3. The down payment is 0.25 (25%) of the cost of the house
4. The cost of the house that you are saving for is $1M.

You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 36 months. 
Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment.

In​ ps1c.py​, write a program to calculate the best savings rate, as a function of your starting salary. 
You should use ​bisection search​ to help you do this efficiently. 
You should keep track of the number of steps it takes your bisections search to finish. 
You should be able to reuse some of the code you wrote for part B in this problem.
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two decimals of 
accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not going to worry about the 
difference between 7.041% and 7.039%). 
This means we can search for an integer​ between 0 and 10000 (using integer division), and then convert it to a decimal 
percentage (using float division) to use when we are calculating the ​current_savings​ after 36 months. 
By using this range, there are only a finite number of numbers that we are searching over, as opposed to the infinite 
number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we use 0 to 10000 is to 
account for two additional decimal places in the range 0% to 100%. 
Your code should print out a decimal (e.g. 0.0704 for 7.04%).

Try different inputs for your starting salary, and see how the percentage you need to save changes to reach your 
desired down payment. Also keep in mind it may not be possible for to save a down payment in a year and a half for 
some salaries. In this case your function should notify the user that it is not possible to save for the down payment 
in 36 months with a print statement. ​
Please make your program print results in the format shown in the test cases below.
Note: There are multiple right ways to implement bisection search/number of steps so your results may not perfectly 
match those of the test case.
"""

# User Inputs

starting_annual_salary = float(input('Enter the starting salary: '))

# Initialize Variables

semi_annual_raise = .07
r = 0.04  # Invest current savings with annual rate of return, r: 4%
portion_down_payment = 0.25  # Portion of the cost needed for a down payment: 25%
total_cost = 1000000  # Cost of dream home: $ 1 Million

# Calculate the rate of savings needed to afford down payment for a home in 3 years (36 months)

cost_down_payment = portion_down_payment * total_cost


def savings_in_3years(best_savings_rate: float, annual_salary: float):
    current_savings = 0
    number_months = 0

    while number_months < 36:
        monthly_investment_return = current_savings * r/12
        monthly_salary_saved = (best_savings_rate/100) * (annual_salary/12)
        current_savings = current_savings + monthly_investment_return + monthly_salary_saved
        number_months = number_months + 1
        if number_months > 0 and number_months % 6 == 0:
            annual_salary = annual_salary + semi_annual_raise * annual_salary

    return current_savings


def bisection_search():

    best_savings_rate_bisection_interval = [0, 10000]
    savings = savings_in_3years(100, starting_annual_salary)

    if savings < cost_down_payment:
        print('It is not possible to pay the down payment in three years')
        return ()

    for steps in range(1, 10000000):
        best_savings_rate = round(sum(best_savings_rate_bisection_interval)/2, 2) * 0.01
        final_savings = savings_in_3years(best_savings_rate, starting_annual_salary)

        tolerance = 100

        if (final_savings >= (cost_down_payment - tolerance)) and (final_savings <= (cost_down_payment + tolerance)):
            print('Best savings rate: ', '{0:.5g}'.format(best_savings_rate * 0.01))
            print('Steps in bisection search: ', steps)
            return ()
        if best_savings_rate_bisection_interval[1] <= best_savings_rate_bisection_interval[0]:
            print('It is not possible to pay the down payment in three years')
            return ()
        if final_savings < (cost_down_payment - tolerance):
            best_savings_rate_bisection_interval[0] = best_savings_rate/0.01
        if final_savings > (cost_down_payment + tolerance):
            best_savings_rate_bisection_interval[1] = best_savings_rate/0.01


bisection_search()
