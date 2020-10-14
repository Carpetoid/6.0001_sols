semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1*10**6
annual_salary = float(input("Enter the starting salary: "))
current_savings = 0
monthly_salary = annual_salary/12   
down_payment = portion_down_payment*total_cost


def check(gues, annual_salary=annual_salary):
    gues /= 10000
    semi_annual_raise = 0.07
    r = 0.04
    current_savings = 0
    monthly_salary = annual_salary/12   
    months_counter = 0 
    for i in range(36):
       months_counter += 1
       current_savings += current_savings*r/12
       current_savings += gues*monthly_salary
       if months_counter % 6 == 0:
          annual_salary += annual_salary*semi_annual_raise
          monthly_salary = annual_salary/12
    return current_savings
    

high = 10000
low = 0
guess = (high+low)//2
epsilon = 100
steps = 1


while abs(check(guess) - down_payment) >= epsilon:
    if check(guess) < down_payment:
        low = guess
    else:
        high = guess
    guess = (high+low)//2
    steps += 1
    if steps > 13:
        print('impossible')
        break
else:
    print("Best savings rate:", str(guess/10000))
    print("Steps in bisection search:", steps)