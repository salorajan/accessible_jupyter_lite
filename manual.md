Accessible Jupyter Lite Pro - Reference Manual

## 1. Application Access and Download
* **Live Web Application:** [Access Accessible Jupyter Lite Pro Here](https://salorajan.github.io/accessible_jupyter_lite/)

## 2. Standard Environment Imports
To use the commands in this manual, ensure these standard imports are at the top of your program window:
```python
import numpy as np
import sympy as sym
import scipy as sci
import matplotlib.pyplot as plt
3. Topic 1: Basic Operations and Constants
The environment allows you to choose between exact symbolic math (SymPy) and fast decimal approximations (NumPy).
1. 
Mathematical Constants:
• 
Symbolic (Exact): sym.pi, sym.E, sym.oo (Infinity)
• 
Numeric (Decimal): np.pi, np.e, np.inf
2. 
Trigonometric Functions:
• 
Symbolic: sym.sin(sym.pi / 2) (Returns exactly 1)
• 
Numeric: np.sin(np.pi / 2) (Returns 1.0)
3. 
Square Roots and Exponents:
• 
Symbolic: sym.sqrt(8) (Returns 2*sqrt(2))
• 
Numeric: np.sqrt(8) (Returns 2.828427)
4. Topic 2: Algebra and Functions
1. 
Defining Symbolic Variables: x, y, z = sym.symbols('x y z')
2. 
Simplifying Expressions: sym.simplify(sym.sin(x)**2 + sym.cos(x)**2)
3. 
Factoring and Expanding:
• 
Factor: sym.factor(x**2 - 4)
• 
Expand: sym.expand((x + 1)**2)
4. 
Solving Algebraic Equations:
• 
Symbolic Exact Roots: sym.solve(x**2 - 5*x + 6, x)
• 
Numeric Polynomial Roots: np.roots([1, -5, 6])
5. Topic 3: Calculus (Derivatives and Integration)
1. 
Derivatives (Differentiation): sym.diff(sym.sin(x) * sym.exp(x), x)
2. 
Indefinite Integrals: sym.integrate(x**2, x)
3. 
Definite Integrals: sym.integrate(x**2, (x, 0, 3))
4. 
Limits: sym.limit(sym.sin(x)/x, x, 0)
6. Topic 4: Vector Calculus
1. 
Setting up a Coordinate System: ```python
from sympy.vector import CoordSys3D
C = CoordSys3D('C')
2. 
Defining a Vector: v = 3*C.i + 4*C.j + 5*C.k
3. 
Gradient: sym.vector.gradient(C.x**2 * C.y * C.z)
4. 
Divergence: sym.vector.divergence(v)
5. 
Curl: sym.vector.curl(v)
7. Topic 5: Matrix Analysis
1. 
Creating Matrices: * Symbolic: M_sym = sym.Matrix([[1, 2], [3, 4]])
• 
Numeric: M_num = np.array([[1, 2], [3, 4]])
2. 
Determinant: M_sym.det() or np.linalg.det(M_num)
3. 
Inverse: M_sym.inv() or np.linalg.inv(M_num)
4. 
Eigenvalues: M_sym.eigenvals() or np.linalg.eig(M_num)
8. Topic 6: Plotting (Matplotlib)
These commands render output directly to the Accessible Figure Window.
1. 
Basic Line Plot: plt.plot(x_vals, y_vals)
2. 
Subplots: fig, (ax1, ax2) = plt.subplots(1, 2)
3. 
Plot Attributes (Crucial for accessibility context): * plt.title("Descriptive Title")
• 
plt.xlabel("X-axis Label")
• 
plt.ylabel("Y-axis Label")
• 
plt.grid(True)
• 
plt.legend()
4. 
Rendering: plt.show() (Must be the final command)
9. Topic 7: Ordinary Differential Equations (ODEs)
1. 
Defining the Function: f = sym.Function('f')
2. 
Defining the Equation: ode = sym.Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sym.sin(x))
3. 
Solving Symbolic ODE: sym.dsolve(ode, f(x))
4. 
Numeric Solution (SciPy): sci.integrate.solve_ivp(function, time_span, initial_conditions)
10. Topic 8: Partial Differential Equations (PDEs)
1. 
Defining Variables: t, x = sym.symbols('t x')
2. 
Defining Function: u = sym.Function('u')
3. 
Defining the PDE (e.g., Heat Equation): pde = sym.Eq(u(t, x).diff(t), u(t, x).diff(x, x))
4. 
Solving Symbolic PDE: sym.pdsolve(pde)
11. Topic 9: Laplace Transforms and Partial Fractions
1. 
Laplace Transform: sym.laplace_transform(sym.sin(t), t, s)
2. 
Inverse Laplace Transform: sym.inverse_laplace_transform(1/(s**2 + 1), s, t)
3. 
Partial Fraction Decomposition: sym.apart(1 / (x**2 + 3*x + 2), x)
12. Topic 10: Optimization (SciPy Analytics)
1. 
Linear Programming: sci.optimize.linprog(c, A_ub, b_ub, bounds)
2. 
Mixed-Integer Linear Programming: sci.optimize.milp(c, integrality, constraints, bounds)
3. 
Differential Evolution (Global Minimum): sci.optimize.differential_evolution(func, bounds)
