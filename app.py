import sympy as sp

# Define variables.
x, y = sp.symbols('x y')

# Solve a simple linear equation 3x - 5 = 16
equation1 = sp.Eq(3*x - 5, 16)
solution1 = sp.solve(equation1, x)
print("Solution to 3x - 5 = 16:", solution1)

# Solve a system of equations.
# x + y = 5
# 2x - y = 1
eq1 = sp.Eq(x + y, 5)
eq2 = sp.Eq(2*x - y, 1)
solution_system = sp.solve((eq1, eq2), (x, y))
print("Solution for the system of equations:", solution_system)

# Solve a quadratic equation x^2 - 5x + 6 = 0
quadratic_eq = sp.Eq(x**2 - 5*x + 6, 0)
solution2 = sp.solve(quadratic_eq, x)
print("Solutions to x^2 - 5x + 6 = 0:", solution2)

