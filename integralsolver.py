import sympy

while True:
    x = sympy.Symbol('x')

    f = input("Enter a function in terms of x: ")
    f = sympy.sympify(f)

    defOrIndef = input("Solve for definite integral (y/n): ")
    if (defOrIndef == "n"):
        indefinite = sympy.integrate(f, x)
        print(f"Indefinite integral of {f}: {indefinite} + C")

    else:
        a = input("Enter the lower bound: ")
        b = input("Enter the upper bound: ")

        if a and b:
            a, b = float(a), float(b)
            definite = sympy.integrate(f, (x, a, b))
            print(f"Definite integral of {f} from {a} to {b}: {definite}")
