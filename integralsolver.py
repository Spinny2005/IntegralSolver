
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import sympy as sp

while True:
    print("")

    def integral_approximation(f, a, b):
        return (int(b)-int(a))*np.mean(f)

    def f(x):
        func = input("Function: ")
        return str(func)

    print("Type u for indefinite integral")
    a = input("Lower Bound: ")
    if (a != "u"):
        b = input("Upper Bound: ")
        x_range = np.arange(int(a),int(b)+0.0001,.0001)
        fx = f(x_range)
        approx = integral_approximation(str(fx),a,b)
        print(approx)
    else:
        func = input("Function: ")
        respect = input("Integrate with respect to: ")
        if (respect != None):
            respect=sp.Symbol(respect)
            result = sp.integrate(func, respect)
            if (result != None):
                print(result)
            else:
                print("Unsolveable Try Again.")
        else:
            print("Unsolveable Try Again.")
