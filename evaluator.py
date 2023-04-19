import re
import numpy as np
import numpy_financial as npf
from finParser import argumentParser

def evaluate(function, inputs):
    R, CF, PV, FV, PMT, NPER = None, [], None, None, None, None

    # TODO: Consider extracting to something in parser, not sure how possible due to constants above.
    for inp in inputs:
        if (match1:= re.match("r = (-?\d*.?\d*)", inp)):
            if R == None:
                R = float(match1.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED A RATE, cannot assign two rates, please provide one.")
            continue

        elif (match2:= re.match("cash_flows = (\[\s*-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s*\])", inp)):
            if len(CF) == 0:
                # DeprecationWarning: string or file could not be read to its end due to unmatched data; this will raise a ValueError in the future.
                CF = np.fromstring(match2.groups()[0].strip(' ]['), dtype=float, sep=',')
            else:
                print("YOU ALREADY ASSIGNED CASH FLOWS, cannot assign two cash flows, please provide one.")

        elif (match3:= re.match("pv = (-?\d*.?\d*)", inp)):
            if PV == None:
                PV = float(match3.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PRESENT VALUE, cannot assign two present values, please provide one.")

        elif (match4:= re.match("fv = (-?\d*.?\d*)", inp)):
            if FV == None:
                FV = float(match4.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PRESENT VALUE, cannot assign two present values, please provide one.")

        elif (match5:= re.match("pmt = (-?\d*.?\d*)", inp)):
            if PMT == None:
                PMT = float(match5.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED PAYMENT, cannot assign two payments, please provide one.")

        elif (match6:= re.match("nper = (\d*.?\d*)", inp)):
            if NPER == None:
                NPER = float(match6.groups()[0])
            else:
                print("YOU ALREADY ASSIGNED NUMBER OF PERIODS, cannot assign two number of periods, please provide one.")

        else:
            print("Invalid argument " + inp)
            print("\n The only valid arguments are: \n \n Rate - defines the rate and can be provided as: \n r = 0.07 or r = 7% or a rate of 2%, etc. \n Cash flows - defines the cash flows(TODO: these descirptions can likely be similar to those of google sheets/excel)) and can be provided as:")


    if function == "NPV":
        while(R == None):
            print("You did not provide a valid rate.") # Add something about what a valid input looks like here
            R_INPUT = input("Please input the rate: ")
            rateExpr = argumentParser("r", R_INPUT)
            match = re.match("r = (-?\d*.?\d*)", rateExpr)
            R = float(match.groups()[0])

        # TODO: DeprecationWarning: elementwise comparison failed; this will raise an error in the future. while(CF == []):
        while(len(CF) == 0):
            print("You did not provide a valid set of cash flows.") # Add something about what a valid input looks like here
            CF_INPUT = input("Please input the cash flows: ")
            cfExpr = argumentParser("cash_flows", CF_INPUT)
            match = re.match("cash_flows = (\[\s?-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s?\])", cfExpr)
            CF = np.fromstring(match.groups()[0].strip(']['), dtype=float, sep=',')

        # TODO: Check that all other values are null, either throw an error if so otherwise just print that it's unnecessary
        else:
            return npf.npv(R, CF)

    elif function == "IRR":
         # TODO: DeprecationWarning: elementwise comparison failed; this will raise an error in the future. while(CF == []):
        while(len(CF) == 0):
            print("You did not provide a valid set of cash flows.") # Add something about what a valid input looks like here
            CF_INPUT = input("Please input the cash flows: ")
            cfExpr = argumentParser("cash_flows", CF_INPUT)
            match = re.match("cash_flows = (\[\s?-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s?\])", cfExpr)
            CF = np.fromstring(match.groups()[0].strip(']['), dtype=float, sep=',')

        # TODO: Check that all other values are null, either throw an error if so otherwise just print that it's unnecessary
        return npf.irr(CF)
        
    elif function == "FV":
        while(R == None):
            print("You did not provide a valid rate.") # TODO: Add something about what a valid input looks like here
            R_INPUT = input("Please input the rate: ")
            rateExpr = argumentParser("r", R_INPUT)
            match = re.match("r = (-?\d*.?\d*)", rateExpr)
            R = float(match.groups()[0])

        while(NPER == None):
            print("You did not provide a valid number of periods.") # TODO: Add something about what a valid input looks like here
            NPER_INPUT = input("Please input the number of periods: ")
            nperExpr = argumentParser("nper", NPER_INPUT)
            match = re.match("nper = (\d*.?\d*)", nperExpr)
            NPER = float(match6.groups()[0])

        while(PMT == None):
            print("You did not provide a valid payment value.") # TODO: Add something about what a valid input looks like here
            PMT_INPUT = input("Please input the payment value: ") #TODO: Note that this will be negative, so a negative value corresponds to a ___ and a positive value corresponds to a ____ 
            pmtExpr = argumentParser("pmt", PMT_INPUT)
            match = re.match("pmt = (-?\d*.?\d*)", pmtExpr)
            PMT = float(match.groups()[0])


        # TODO: Check that all other values are null (caution w/PV), either throw an error if so otherwise just print that it's unnecessary
        if PV == None:
            return npf.fv(R, NPER, PMT)
        
        else:
            return npf.fv(R, NPER, PMT, PV)
    
    elif function == "PV":
        while(R == None):
            print("You did not provide a valid rate.") # TODO: Add something about what a valid input looks like here
            R_INPUT = input("Please input the rate: ")
            rateExpr = argumentParser("r", R_INPUT)
            match = re.match("r = (-?\d*.?\d*)", rateExpr)
            R = float(match.groups()[0])

        while(NPER == None):
            print("You did not provide a valid number of periods.") # TODO: Add something about what a valid input looks like here
            NPER_INPUT = input("Please input the number of periods: ")
            nperExpr = argumentParser("nper", NPER_INPUT)
            match = re.match("nper = (\d*.?\d*)", nperExpr)
            NPER = float(match6.groups()[0])

        while(PMT == None):
            print("You did not provide a valid payment value.") # TODO: Add something about what a valid input looks like here
            PMT_INPUT = input("Please input the payment value: ") #TODO: Note that this will be negative, so a negative value corresponds to a ___ and a positive value corresponds to a ____ 
            pmtExpr = argumentParser("pmt", PMT_INPUT)
            match = re.match("pmt = (-?\d*.?\d*)", pmtExpr)
            PMT = float(match.groups()[0])


        # TODO: Check that all other values are null (caution w/FV), either throw an error if so otherwise just print that it's unnecessary
        if FV == None:
            return npf.pv(R, NPER, PMT)
        else:
            return npf.pv(R, NPER, PMT, FV)    

    else:
        # TODO: Give a better error message
        return "ERROR"
    
    # Example that currently works:
    # Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?
