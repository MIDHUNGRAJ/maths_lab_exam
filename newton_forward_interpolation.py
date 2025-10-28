# Newton's Forward Interpolation

def forward_difference_table(x, y):
    """
    Constructs the forward difference table for the given data points.
    
    Args:
        x (list): A list of x-values.
        y (list): A list of y-values.
        
    Returns:
        tuple: A tuple containing the x-values, the y-values (which are modified to contain the forward differences),
               and the value 'h' (the constant interval between x-values).
    """
    n = len(y)
    
    # Create a copy of y to avoid modifying the original list if it's not needed elsewhere
    y_copy = list(y)
    
    # Compute the forward differences
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y_copy[i] = y_copy[i] - y_copy[i - 1]
            
    # Calculate h (constant interval)
    h = x[1] - x[0]
    
    return x, y_copy, h

def newton_forward_interpolation(x, y, x_interp):
    """
    Performs Newton's forward interpolation.
    
    Args:
        x (list): A list of x-values.
        y (list): A list of y-values.
        x_interp (float): The value at which to interpolate.
        
    Returns:
        float: The interpolated value.
    """
    x_vals, diff_table, h = forward_difference_table(x, y)
    
    # Calculate u
    u = (x_interp - x_vals[0]) / h
    
    # Initialize the interpolated value with the first y-value
    interp_value = diff_table[0]
    
    n = len(x_vals)
    # Calculate the terms of the Newton's formula and add them to the sum
    for i in range(1, n):
        # Calculate the i-th term of the formula
        # This is the numerator of the fraction: u * (u-1) * ... * (u-i+1)
        numerator = 1.0
        for j in range(i):
            numerator = numerator * (u - j)
            
        # Calculate the factorial of i
        factorial_i = 1.0
        for j in range(1, i + 1):
            factorial_i = factorial_i * j
            
        # Add the term to the interpolated value
        interp_value = interp_value + (numerator / factorial_i) * diff_table[i]
        
    return interp_value

# Example usage from the image
# You can change these values to your own data
x_data = [1, 3, 5, 7]
y_data = [24, 120, 336, 720]  # Example: y = x^3
interpolation_point = 2     # The point to interpolate at

# Perform interpolation
interpolated_y = newton_forward_interpolation(x_data, y_data, interpolation_point)

# Print the result
print(f"The interpolated value at x = {interpolation_point} is approximately: {interpolated_y}")
