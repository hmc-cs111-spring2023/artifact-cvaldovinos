import re
import numpy as np
import numpy_financial as npf

def evaluate(function, inputs):
    r, cash_flows, pv, fv, pmt, nper = None, None, None, None, None, None

    for inp in inputs:
        if (match1:= re.match("r = (-?\d*.?\d*)", inp)):
            if r == None:
                r = float(match1.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED A RATE, cannot assign two rates, please provide one.")
            continue
        
        
        elif (match2:= re.match("cash_flows = (\[-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\])", inp)):
            if cash_flows == None:
                # DeprecationWarning: string or file could not be read to its end due to unmatched data; this will raise a ValueError in the future.
                cash_flows = np.fromstring(match2.groups()[0].strip(']['), dtype=float, sep=',')
            else:
                print("YOU ALREADY ASSIGNED CASH FLOWS, cannot assign two cash flows, please provide one.")

        elif (match3:= re.match("pv = (-?\d*.?\d*)", inp)):
            if pv == None:
                pv = float(match3.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PRESENT VALUE, cannot assign two present values, please provide one.")
        
        elif (match4:= re.match("fv = (-?\d*.?\d*)", inp)):
            if fv == None:
                fv = float(match4.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PRESENT VALUE, cannot assign two present values, please provide one.")

        elif (match5:= re.match("pmt = (-?\d*.?\d*)", inp)):
            if pmt == None:
                pmt = float(match5.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PAYMENT, cannot assign two payments, please provide one.")

        elif (match6:= re.match("nper = (\d*.?\d*)", inp)):
            if nper == None:
                nper = float(match6.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED NUMBER OF PERIODS, cannot assign two number of periods, please provide one.")
        
        else:
            print("Invalid argument " + inp)
            print("\n The only valid arguments are: \n \n Rate - defines the rate and can be provided as: \n r = 0.07 or r = 7% or a rate of 2%, etc. \n Cash flows - defines the cash flows(TODO: these descirptions can likely be similar to those of google sheets/excel)) and can be provided as:")



    if function == "NPV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to npv
        # return npv(inputs[0], inputs[1])

        return npf.npv(r, cash_flows)

    elif function == "IRR":
        # TODO:
        # I should check that there is only one input for IRR
        return npf.irr(cash_flows)
        
    elif function == "FV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to fv
        # return fv(inputs[0], inputs[1], inputs[2], inputs[3])
        # CAUTION: PV is optional
        if pv == None:
            return npf.fv(r, nper, pmt)
        else:
            return npf.fv(r, nper, pmt, pv)
        # Check for inputs
        # Convert inputs to call to fv
    
    elif function == "PV":
        # TODO:
        # Check for inputs
        # Convert inputs to call to pv
        # return pv(inputs[0], inputs[1], inputs[2], inputs[3])
        # CAUTION: FV is optional
        if fv == None:
            return npf.pv(r, nper, pmt)
        else:
            return npf.pv(r, nper, pmt, fv)    

    else:
        #Give a better error message
        return "ERROR"
    
    # Example that currently works:
    # Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?
