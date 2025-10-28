# Newton Backward Interpolation in SageMath

# Define the data points
x = [1, 2, 3, 4, 5]            
y = [2, 8, 27, 64, 125]        

# Point to estimate
xp = 3.5                      

# Number of data points
n = len(x)

# Create a table for backward differences
diff_table = [[0 for i in range(n)] for j in range(n)]

# Fill the first column with y values
for i in range(n):
    diff_table[i][0] = y[i]

# Compute backward differences
for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

# Display backward difference table
print('Backward Difference Table:')
for i in range(n):
    print(diff_table[i][:i+1])

# Compute u
h = x[1] - x[0]
u = (xp - x[-1]) / h

# Evaluate the interpolation polynomial
interp = diff_table[n - 1][0]
u_term = 1

for j in range(1, n):
    u_term = u_term * (u + j - 1)
    interp = interp + (u_term * diff_table[n - 1][j]) / factorial(j)

print(f"Estimated value at x = {xp} is {interp.n()}") 

# Optional: Create symbolic backward interpolation polynomial
var('X')
u_sym = (X - x[-1]) / h
poly = diff_table[n - 1][0]
u_term = 1

for j in range(1, n):
    u_term = u_term * (u_sym + j - 1)
    poly = poly + (u_term * diff_table[n - 1][j]) / factorial(j)

poly = expand(poly)
print(f"Interpolating Polynomial:\n{poly}")
show(poly)
