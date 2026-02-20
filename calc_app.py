import dummycalc as dc

menu = """
1) Add
2) Subtract
3) Multiply
4) Divide
5) Power
6) Square Root
7) Factorial
8) Quick Report
0) Exit
"""

while True:
    print(menu)
    choice = input("Choose: ").strip()

    if choice == "0":
        break

    try:
        if choice in {"1","2","3","4","5","8"}:
            a = float(input("a: "))
            b = float(input("b: "))

        if choice == "1":
            print(dc.add(a, b))
        elif choice == "2":
            print(dc.subtract(a, b))
        elif choice == "3":
            print(dc.multiply(a, b))
        elif choice == "4":
            print(dc.divide(a, b))
        elif choice == "5":
            print(dc.power(a, b))
        elif choice == "6":
            x = float(input("x: "))
            print(dc.square_root(x))
        elif choice == "7":
            n = float(input("n (integer): "))
            print(dc.factorial(n))
        elif choice == "8":
            print(dc.quick_report(a, b))
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", type(e).__name__, "-", e)