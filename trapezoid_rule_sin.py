# Define the function
f(x) = sin(x)

# Set the interval and number of trapezoids
a = 0
b = 1
n = 10

# Implement the trapezoidal rule function
def trapezoid_rule(fcn, a, b, n):
    h = (b-a)/n  # Calculate the width of each trapezoid
    
    # Create a list of function values at each point
    vals = [fcn(a + i*h) for i in range(n+1)]
    
    # Apply the trapezoidal rule formula
    return (h/2) * (vals[0] + 2*sum(vals[1:n]) + vals[n])

# Call the function and print the result
print(trapezoid_rule(f, a, b, n).n())
