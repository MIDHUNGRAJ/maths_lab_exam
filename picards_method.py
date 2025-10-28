# Define the function f(x, y)
var('x, y')
f = x + y^2

# Initial condition
x0 = 0  # Initial x value
y0 = 0  # Initial y value (y(x0) = y0)

# Picard iteration setup
y = y0  # Start with the initial approximation y_0(x) = y0
iterations = 2  # Number of iterations

# Perform Picard iterations
for i in range(iterations):
    y = y0 + integrate(f.substitute(y=y), x, x0, x)  # Update y using the integral of f
    print(f"Iteration {i+1}: y_{i+1}(x) = {y}")
