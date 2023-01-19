import streamlit as st
import numpy as np
from scipy.optimize import linprog

st.title('Linear Programming Solver')

# Define objective function
c = st.multiselect('Select the coefficients of the objective function:', options=[i for i in range(-10, 11)])
c = np.array(c, dtype=float)

# Define constraints
A = []
b = []
st.write('Enter the coefficients of the constraints')
for i in range(1, st.slider('Number of constraints', min_value=1, max_value=10, value=2) + 1):
    row = st.multiselect(f'Constraint {i}', options=[i for i in range(-10, 11)])
    A.append(row)
    b.append(st.number_input(f'RHS of constraint {i}', min_value=-100, max_value=100, value=0))

# Define bounds
x_bounds = []
st.write('Enter the bounds of the variables')
for i in range(1, len(c) + 1):
    x_bounds.append((st.number_input(f'Lower bound of x{i}', min_value=-100, max_value=100, value=-10),
                     st.number_input(f'Upper bound of x{i}', min_value=-100, max_value=100, value=10)))

# Solve linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='revised simplex')

# Print results
if res.success:
    st.write('Optimal solution found')
    st.write(f'Optimal value: {res.fun}')
    st.write(f'Optimal variables: {res.x}')
else:
    st.write('Solution not found')
