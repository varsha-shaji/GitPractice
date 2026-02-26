import sys

try:
    a = int(input("Enter first Number :"))
    b = int(input("Enter Second Number:"))
    ch = input("Enter a operation (+,-,*,/): ")
    if ch == "+":
        res = a + b

    elif ch == "-":
        res = a - b

    elif ch == "*":
        res = a * b
    elif ch == "/":
        try:
            res = a / b
d
        except:
            print(sys.exc_info())
            sys.exit(1)
    else:
        print("invalid operation")
    print("{0} {1} {2} is {3}".format(a, ch, b, res))

except:
    print(sys.exc_info())