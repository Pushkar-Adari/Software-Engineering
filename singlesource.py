def solve_eqn(coefficient,x):
    a,b,c = coefficient
    return a*x**2 + b*x + c 
coefficient = float(input("a,b,c: "))
x = float(input("x: "))
result = solve_eqn(coefficient,x)
print({result})