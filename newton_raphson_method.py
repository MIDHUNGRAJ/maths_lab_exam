# Define variable and function
var('x')
f(x) = x*exp(x) - 1          # f(x) = x*e^x - 1
fprime(x) = diff(f, x)       # derivative f'(x)

# Newton-Raphson function
def newton(f, fprime, x0, tol=1e-10, max_iter=20):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/fprime(x)
        print(f"Iter {i+1}: x = {n(x_new, digits=12)}")
        if abs(x_new - x) < tol:
            print(f"\nConverged after {i+1} iterations.")
            return n(x_new, digits=12)
        x = x_new
    print("\nDid not converge.")
    return n(x, digits=12)

# Initial guess x0 = 1 (as in the example)
x_root = newton(f, fprime, 1)
print(f"\nApproximate root: {x_root}")

# Compare with analytical value using Lambert W
x_exact = lambert_w(1)
print(f"Exact root using Lambert W: {n(x_exact, digits=12)}")
