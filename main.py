from finParser import parse

# You can run this file with
# 
#  python main.py


# When prompted in the terminal you can input strings of the following 3 formats:
#       Given W, X, Y, and Z. What is the A?
#       Given X and Y. What is the A?
#       Given X. What is the A?
# 
#       Where A is one of the following:
#           - Net Present Value / NPV           (All characters can be lowercase)
#           - Future Value / FV                 (All characters can be lowercase)
#           - Internal Rate of Return / IRR     (All characters can be lowercase)
#           - Present Value / PV                (All characters can be lowercase)

# This will output the "inputs" and the "function name" which the parser returns from the input string.

# TODO: Throw errors for when the given statement is invalid.

def main():
    while True:
        text = input('FinanceCalculator > ')

        if text == "exit" or text == "quit":
            print("Exiting FinanceCalculator...")
            break

        inputs, functionName = parse(text)
        print("Inputs:       ", inputs)
        print("Function Name:", functionName)

if __name__ == "__main__":
    main()
