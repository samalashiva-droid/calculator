try:
    a = int(input("Enter the first number: "))

    b = int(input("Enter the first number: "))

    print("what kind of operation do you want to perform.press + for addition\npress - for subtraction\npress / for division\npress * for multiplication")

    o = input("Enter opration: ")
    match o:
        case "+":
            print(f"the result is: {a + b}")
        case "-":
            print(f"the result is: {a - b}")
        case "*":
            print(f"the result is: {a * b}")
        case "/":
            print(f"the result is: {a / b}")
        case default:
            print(f"there was an error")

except Exception as e:
    print("Enter a valid value of a and b")

