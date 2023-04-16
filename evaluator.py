import re
from numpy_financial import npv, irr, fv, pv

def evaluate(function, inputs):
    if function == "NPV":
        # Check for inputs
        # Convert inputs to call to npv
        return npv(inputs[0], inputs[1])
    elif function == "IRR":
        # I should check that there is only one input for IRR
        match = re.match("cash_flows = (\[.*\])", inputs[0])

        if match:
            operation = list(filter(lambda x: x != None, match.groups()))
            return irr(operation[0].strip('][').split(', '))
        
        else:
            return "ERROR"
        
    elif function == "FV":
        # Check for inputs
        # Convert inputs to call to fv
        return fv(inputs[0], inputs[1], inputs[2], inputs[3])
    
    elif function == "PV":
        # Check for inputs
        # Convert inputs to call to npv
        return pv(inputs[0], inputs[1], inputs[2], inputs[3])
    
    else:
        #Give a better error message
        return "ERROR"
    
    # Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?
