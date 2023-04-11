def calculator():
    num1 = float(input("Enter Your First Number: "))
    num2 = float(input("Enter Your Second Number: "))
    op = input("Enter Operators(+, -, *, /: )")
    if op == '+':
        result = num1 + num2
        print("Your Output Is: ", result)
    elif op == '-':
        result = num1 - num2
        print("Your Output Is: ", result)
    elif op == '*':
        result = num1 * num2
        print("Your Output Is: ", result)
    elif op == '/':
        result = num1 / num2
        print("Your Output Is: ", result)
    else:
        print("Invalid Input")
        return
if __name__ == "__main__":
     calculator()