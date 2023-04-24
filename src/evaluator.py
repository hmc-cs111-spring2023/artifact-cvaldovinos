import re
import numpy as np
import numpy_financial as npf
from finParser import argumentParser

def evaluate(function, inputs):
    R, CF, PV, FV, PMT, NPER = None, [], None, None, None, None
    tooManyArgs = False

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
                print("YOU ALREADY ASSIGNED FUTURE VALUE, cannot assign two future values, please provide one.")

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
            print("Invalid argument: " + inp + "\n The only valid arguments are: \n \n Rate - defines the rate and can be provided as: \n r = 0.07 or r = 7% or a rate of 2%, etc. \n Cash flows - defines the cash flows(TODO: these descriptions can likely be similar to those of google sheets/excel) and can be provided as:")
            return
            # TODO: Add some while loop here or figure out what happens to the user if they provide an invalid argument.
            #       I think this case might not even be reachable but would need to ensure that parser previously catches all args.

    if function == "NPV":
        while(R == None):
            print("You did not provide a valid rate.") # Add something about what a valid input looks like here
            R_INPUT = input("Please input the rate: ")
            rateExpr = argumentParser("r", R_INPUT)
            match = re.match("r = (-?\d*.?\d*)", rateExpr)
            R = float(match.groups()[0])

        while(len(CF) == 0):
            print("You did not provide a valid set of cash flows.") # Add something about what a valid input looks like here
            CF_INPUT = input("Please input the cash flows: ")
            cfExpr = argumentParser("cash_flows", CF_INPUT)
            match = re.match("cash_flows = (\[\s?-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s?\])", cfExpr)
            CF = np.fromstring(match.groups()[0].strip(']['), dtype=float, sep=',')

        if FV != None:
            tooManyArgs = True
            print("You provided a future value but NPV does not use future value so that argument was ignored.")
        if PV != None:
            tooManyArgs = True
            print("You provided a present value but NPV does not use present value so that argument was ignored.")
        if PMT != None:
            tooManyArgs = True
            print("You provided a payment value but NPV does not use payment value so that argument was ignored.")
        if NPER != None:
            tooManyArgs = True
            print("You provided a number of periods but NPV does not use number of periods so that argument was ignored.")
        if tooManyArgs:
            print("NPV only uses 2 arguments: rate and cash flows.\n\n")

        return npf.npv(R, CF)

    elif function == "IRR":
        while(len(CF) == 0):
            print("You did not provide a valid set of cash flows.") # Add something about what a valid input looks like here
            CF_INPUT = input("Please input the cash flows: ")
            cfExpr = argumentParser("cash_flows", CF_INPUT)
            match = re.match("cash_flows = (\[\s?-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s?\])", cfExpr)
            CF = np.fromstring(match.groups()[0].strip(']['), dtype=float, sep=',')

        if FV != None:
            tooManyArgs = True
            print("You provided a future value but IRR does not use future value so that argument was ignored.")
        if PV != None:
            tooManyArgs = True
            print("You provided a present value but IRR does not use present value so that argument was ignored.")
        if PMT != None:
            tooManyArgs = True
            print("You provided a payment value but IRR does not use payment value so that argument was ignored.")
        if NPER != None:
            tooManyArgs = True
            print("You provided a number of periods but IRR does not use number of periods so that argument was ignored.")
        if R != None:
            tooManyArgs = True
            print("You provided a rate but IRR does not use rate so that argument was ignored.")
        if tooManyArgs:
            print("IRR only uses 1 argument: cash flows.\n\n")

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

        if FV != None:
            tooManyArgs = True
            print("You provided a future value but FV does not use future value so that argument was ignored.")
        if len(CF) != 0:
            tooManyArgs = True
            print("You provided cash flows but FV does not use cash flows so that argument was ignored.")
        if tooManyArgs:
            print("FV only needs 3 arguments: rate, number of periods, and payment value. OPTIONALLY you can add a present value \n\n")

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

        if PV != None:
            tooManyArgs = True
            print("You provided a present value but PV does not use present value so that argument was ignored.")
        if len(CF) != 0:
            tooManyArgs = True
            print("You provided cash flows but PV does not use cash flows so that argument was ignored.")
        if tooManyArgs:
            print("PV only needs 3 arguments: rate, number of periods, and payment value. OPTIONALLY you can add a future value \n\n")

        if FV == None:
            return npf.pv(R, NPER, PMT)
        else:
            return npf.pv(R, NPER, PMT, FV)    

    else:
        # TODO: Give a better error message
        return "ERROR"
