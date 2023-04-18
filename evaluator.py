import re
from numpy_financial import npv, irr, fv, pv

def evaluate(function, inputs):
    if function == "NPV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to npv
        # return npv(inputs[0], inputs[1])
        print("function: " + function)
        print("inputs: " + str(inputs))
        return "NOT IMPLEMENTED"

    elif function == "IRR":
        # TODO:
        # I should check that there is only one input for IRR
        match = re.match("cash_flows = (\[.*\])", inputs[0])

        if match:
            operation = list(filter(lambda x: x != None, match.groups()))
            return irr(operation[0].strip('][').split(', '))
        
        else:
            return "ERROR"
        
    elif function == "FV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to fv
        # return fv(inputs[0], inputs[1], inputs[2], inputs[3])

        print("function: " + function)
        print("inputs: " + str(inputs))
        return "NOT IMPLEMENTED"
        # Check for inputs
        # Convert inputs to call to fv
    
    elif function == "PV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to pv
        # return pv(inputs[0], inputs[1], inputs[2], inputs[3])

        print("function: " + function)
        print("inputs: " + str(inputs))
        return "NOT IMPLEMENTED"
    
    else:
        #Give a better error message
        return "ERROR"
    
    # Example that currently works:
    # Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?
