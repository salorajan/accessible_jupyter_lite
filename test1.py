import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve
from scipy.optimize import linprog, milp, differential_evolution, LinearConstraint, Bounds

# 1. Initialization and Input Test
print("=== 1. Welcome to the Accessible Jupyter Lite Pro Feature Test ===")
print("1.1. System check initiated. Numpy, Sympy, Matplotlib, and Scipy imported successfully.")

user_name = input("1.2. Interactive Prompt: Please type your name and press enter to begin:")
print(f"1.3. Hello, {user_name}! Input received successfully. Initiating Scipy optimization sequence.")

# 2. SciPy Linear Programming (linprog)
print("\n=== 2. SciPy Linear Programming Phase ===")
print("2.1. Scenario: Minimizing the function Z = -3x - 4y.")
print("2.2. Subject to constraints: x + 2y <= 14, 3x - y >= 0, x - y <= 2.")

# Coefficients for the objective function (minimization)
c_lp = [-3, -4]
# Inequality constraint matrix (Left side)
A_ub = [[1, 2], [-3, 1], [1, -1]]
# Inequality constraint vector (Right side)
b_ub = [14, 0, 2]

res_lp = linprog(c_lp, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))
print(f"2.3. Optimal Function Value: {res_lp.fun:.2f}")
print(f"2.4. Optimal Variables (x, y): {res_lp.x}")

# 3. SciPy Mixed-Integer Linear Programming (milp)
print("\n=== 3. SciPy Mixed-Integer Linear Programming Phase ===")
print("3.1. Scenario: Same minimization problem as above, but x and y MUST be integers.")

# Define integrality constraints (1 means the variable must be an integer)
integrality = [1, 1] 
constraints = LinearConstraint(A_ub, -np.inf, b_ub)
res_milp = milp(c=c_lp, constraints=constraints, integrality=integrality, bounds=Bounds(0, np.inf))

print(f"3.2. Optimal Integer Function Value: {res_milp.fun:.2f}")
print(f"3.3. Optimal Integer Variables (x, y): {res_milp.x}")

# 4. SciPy Differential Evolution
print("\n=== 4. SciPy Differential Evolution Phase ===")
print("4.1. Scenario: Finding the global minimum of the non-linear function y = x^2 + x * sin(x).")

# Define the non-linear objective function
def objective_func(x):
    return x[0]**2 + x[0] * np.sin(x[0])

# Define search bounds for x between -10 and 10
bounds_de = [(-10, 10)]
res_de = differential_evolution(objective_func, bounds_de)

print(f"4.2. Global Minimum Function Value (y): {res_de.fun:.4f}")
print(f"4.3. Optimal Variable Location (x): {res_de.x[0]:.4f}")

# 5. Matplotlib Figure Generation
print("\n=== 5. Matplotlib Figure Generation Phase ===")
print("5.1. Audio Description: Rendering the differential evolution function.")
print("5.2. The plot will show a parabola-like curve with a slight wave due to the sine function.")
print("5.3. A red dot will mark the exact global minimum discovered by the differential evolution algorithm.")

x_vals = np.linspace(-10, 10, 200)
y_vals = x_vals**2 + x_vals * np.sin(x_vals)

plt.plot(x_vals, y_vals, label="y = x^2 + x*sin(x)", color="blue", linewidth=2)
plt.plot(res_de.x[0], res_de.fun, 'ro', markersize=8, label="Global Minimum")
plt.title(f"{user_name}'s Differential Evolution Optimization")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.legend()
plt.show()

# 6. UI Navigation and Shortcut Testing
print("\n=== 6. Manual UI Feature Verification ===")
print("6.1. The visual plot has been routed to the Figure Window.")
print("6.2. Please test the following application controls to verify functionality:")
print("6.3. Action 1: Press Alt + 3 to navigate to the Figure Window.")
print("6.4. Action 2: Activate the '5. Download Command Output' button.")
print("6.5. Action 3: Activate the '6. Download Plot Figure' button.")
print("6.6. Action 4: Activate the '4. Clear Command & Figure' button. Verify both regions empty out.")
print("6.7. Action 5: Activate the '3. Clear Program Window' button. Verify your code vanishes and focus returns to the editor.")
print("6.8. Action 6: Type 'print(100)' into the empty Program Window and press Control + Enter to verify your new execution shortcut.")
print("=== End of Test Sequence ===")