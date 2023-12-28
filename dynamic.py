a = float(input("Enter 1st coefficient: "))
b = float(input("Enter 2nd coefficient: "))
c = float(input("Enter 3rd coefficient: "))
x = float(input("Enter value of X: "))

def w_m(x):
    return a*x**2 + b*x + c 
print(w_m(3))