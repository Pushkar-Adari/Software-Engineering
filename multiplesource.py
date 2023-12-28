def solve_eqn(a,b,c,x):
    return a*x**2 + b*x + c 
num_sets = int(input("Coefficient: "))
x = float(input("x: "))
for i in range(num_sets):
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    result = solve_eqn(a,b,c,x)