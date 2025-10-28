# Simpson's 1/3rd Rule for a given function

# Import symbolic tools
var('x')

# Define the function here
f(x) = x^3 + 2*x^2 + 3*x + 1   # Example function

# Define integration limits and number of intervals (n must be even)
a = 0
b = 4
n = 6

# Step size
h = (b - a) / n

# Compute Simpson's 1/3 rule
sum_odd = sum([f(a + i*h) for i in range(1, n, 2)])
sum_even = sum([f(a + i*h) for i in range(2, n, 2)])

I = (h/3) * (f(a) + 4*sum_odd + 2*sum_even + f(b))

print(f"Using Simpson's 1/3rd Rule:")
print(f"Approximate integral from {a} to {b} is {I.n()}") # .n() for numerical value

# Optional: Compute exact integral and error
I_exact = integrate(f(x), x, a, b)
print(f"Exact integral = {I_exact.n()}")
print(f"Error = {abs(I.n() - I_exact.n())}")
