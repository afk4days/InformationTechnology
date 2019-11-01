num1 = int(input("Enter Number 1: "))
oper = input("Enter The Operator: ")
if oper == "*" or "/" or "+" or "-":
    num2 = int(input("Enter Number 2: "))
    if oper == "*":
        ans = num1 * num2
    elif oper == "/":
        ans = num1 / num2
    elif oper == "+":
        ans = num1 + num2
    elif oper == "-":
        ans = num1 - num2
    print(num1, oper, num2, "=", ans)
elif oper != "*" or "/" or "+" or "-":
    print("Math Error")