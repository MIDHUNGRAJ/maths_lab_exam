# Define a symbolic variable and a polynomial ring
x = var('x')
R = PolynomialRing(QQ, x)

# Define the data points as a list of (x, y) tuples
points = [(0, 1), (1, 7), (2, 23), (3, 55), (4, 109)]

# Create the Lagrange interpolating polynomial
interpolating_poly = R.lagrange_polynomial(points)

# Display the resulting polynomial
print(f"The interpolating polynomial is: {interpolating_poly}")

# Evaluate the polynomial at the desired point
interpolated_value = interpolating_poly(x=0.5)
print(f"The interpolated value at x=0.5 is: {interpolated_value}")
