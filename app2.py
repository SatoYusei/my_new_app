import streamlit as st
from scipy.optimize import minimize_scalar

def newton_method(fun, x0):
    res = minimize_scalar(fun, bracket=(x0-1, x0+1), options={'xtol': 1e-8, 'disp': False}, method='golden')
    return res.x

def optimize_app():
    st.title("Newton Method Optimization App")

    fun = st.text_input("Enter a function in terms of x:")
    x0 = st.number_input("Enter the initial value:")

    if st.button("Optimize"):
        try:
            fun = lambda x : x*x
            result = newton_method(fun, x0)
            st.success("Minimum is at x = {}".format(result))
        except:
            st.error("Invalid function or initial value.")

if __name__ == '__main__':
    optimize_app()
