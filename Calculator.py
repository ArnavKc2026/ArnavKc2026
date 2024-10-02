def calc(operator, num1, num2):
    #Make sure the inputs are numbers
    if not isinstance(num1, (int, float)):
        raise ValueError(f'Invalid value "{num1}"')
    if not isinstance(num2, (int, float)):
        raise ValueError (f'Invalid value "{num2}"')
    
    #Do the acutal calculations with different operators
    if operator in ('+', 'add'):
        return num1 + num2
    elif operator in ('-', 'sub'):
        return num1 - num2
    elif operator in ('*', 'mul'):
        return num1 * num2
    elif operator in ('/', 'div'):
        if num2 == 0:
            raise ZeroDivisionError("Dividing by zero")
        return num1 / num2
    elif operator in ('%', 'mod'):
        return num1 % num2
    elif operator in ('^', 'pow'):
        return num1 ** num2
    
    else:
        raise ValueError(f'Not an operator "{operator}"')

def get_num():
    #The function so users are able to enter what type of operator and number to enter
    operator = input("Enter an operation:")
    try:
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
    except ValueError as e:
        raise ValueError("Invalid numbers. Try again. ") from e
    
    return operator, num1, num2

#This is the main function so the calculator will run
def main():
    print("Welcome to calculator")

    while True:
        user_input = input("You want to do a calculation?")
        if user_input == 'exit':
            print("See you later")
            break
        elif user_input == 'yes':
            try:
                operator, num1, num2 = get_num()
                result = calc(operator, num1, num2)
                print(f"The result of {num1} {operator} {num2} is: {result}\n")
            
            except ValueError as ve:
                print(f"Mistake: {ve}")
            except ZeroDivisionError as zde:
                print(f"Mistake: {zde}")

        else:
            print("Type 'yes' to continue or 'exit' to quit")

if __name__ == "__main__":
    main()