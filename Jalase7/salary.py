def salary(exp, edu, job, base_salary = 20000000):
    salary = base_salary
    salary = salary + .1 * exp * salary
    edu_grade = {
        'phd':.4,
        'ms':.3,
        'bc':.2
    }.get(edu, 0)
    salary = salary + edu_grade * salary
    if job == 1:
        salary += .2 * salary
        return salary



def taxt(salary):
    tax = 0
    if salary >= 40000000:
            tax += (salary - 40000000) * .1
    return tax

def insu(salary):
     return salary * .7

def net_salary(salary):
     return salary - tax(salary) - insu(salary)

p1_salary = salary(20, 'ms', 1)
p1_net_salary = net_salary(p1_salary)
print(f'p1 salary = {p1_salary} , net salary = {p1_net_salary}')