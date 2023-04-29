import numpy_financial as npf;
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]) / "src")
from finParser import parse
from evaluator import evaluate

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

def main():
    while True:
        text = input('\nFinanceCalculator > ')

        if text == "exit" or text == "quit":
            print("Exiting FinanceCalculator...")
            break

        inputs, functionName = parse(text)

        invalidInput = (inputs == None or functionName == None)
        if invalidInput: continue
        
        elif "ERROR: Invalid input." in inputs:
            print("\nERROR: Invalid input name found.\n\nAllowed inputs include rate, nper, pmt, pv, fv, and cash flows.")

        elif functionName == "Invalid Function Name":
            print("\nERROR: No valid function name found.\n\nAllowed function names include: NPV, FV, IRR, and PV.\n")

        else:
            print("")
            print(evaluate(functionName, inputs))
            print("")

if __name__ == "__main__":
    main()
