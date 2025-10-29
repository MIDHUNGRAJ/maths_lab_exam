def bisection_method(f, a, b, eps):
    intervals = [(a,b)]
    two = float(2)
    eps = float(eps)
    while True:
        c = (a+b)/two
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if abs(fc) < eps:
            return c, intervals
        if fa*fc < 0:
            a, b = a, c
        elif fc*fb < 0:
            a, b = c, b
        else:
            raise ValueError("f must have a sign change in the interval (%s,%s)"%(a,b))
        intervals.append((a,b))

#Example 5: Display interval progression
def f5(x):
    return x**3 - 4
print("Example 5: Interval progression for x^3 - 4 = 0")
root5, intervals5 = bisection_method(f5, 1, 2, 0.01)
for i, interval in enumerate(intervals5):
    print(f"Iteration {i}: [{interval[0]:.6f}, {interval[1]:.6f}]")
print(f"Final root: {root5}")

