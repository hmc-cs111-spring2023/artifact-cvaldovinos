import re

def format_operations(string):
    """This function removes the 'Given', 'and', and spaces from the start of
        operations."""
    
    # This statement works when there are 3 or more operations.
    return re.sub("(Given )?(^\s+)?(and )?", "", string)

def format_operations1(string):
    """This function removes the 'Given', 'and', and spaces from the start of
        operations."""
    
    # This statement works when there are 2 or less operations.
    return re.sub("(Given )?(^\s+)?(and )?", "", string)

def inputFormatter(match, variable):        
    """This function formats the input into valid Python code."""

    operation = list(filter(lambda x: x != None, match.groups()))
    if "%" in operation[0]:
        match1 = re.match("(\d*).?(\d*)\%?", operation[0])
        groups = list(match1.groups())
        
        while len(groups[0]) < 2:
            groups[0] = "0" + groups[0]

        while len(groups[1]) < 2:
            groups[1] = groups[1] + "0"
        
        i = len(groups[0]) - 2
        operation[0] = groups[0][0:i] + "." + groups[0][i:] + groups[1]
    
    if (len(operation) == 2):
        return variable + " = " + str(eval(operation[0] + operation[1]))
    else:
        return variable + " = " + str(eval(operation[0]))

def operationParser(string):
    """This function determines which input each operation corresponds to."""

    matchesRateExpr1 = re.match("a?\s?rate of (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr1: return inputFormatter(matchesRateExpr1, "r")

    matchesRateExpr2 = re.match("a?\s?rate = (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr2: return inputFormatter(matchesRateExpr2, "r")
        
    matchesRateExpr3 = re.match("a?\s?r = (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr3: return inputFormatter(matchesRateExpr3, "r")

    matchesNperExpr1 = re.match("(\d*)(\*\d*)? periods", string)
    if matchesNperExpr1: return inputFormatter(matchesNperExpr1, "nper")

    matchesNperExpr2 = re.match("nper = (\d*)(\*\d*)?", string)
    if matchesNperExpr2: return inputFormatter(matchesNperExpr2, "nper")

    matchesNperExpr3 = re.match("nper of (\d*)(\*\d*)?", string)
    if matchesNperExpr3: return inputFormatter(matchesNperExpr3, "nper")

    matchesPmtExpr1 = re.match("\$(-?\d*\.?\d+) payments", string)
    if matchesPmtExpr1: return "pmt = -" + matchesPmtExpr1.group(1)

    matchesPmtExpr2 = re.match("pmt = (-?\d*\.?\d+)", string)
    if matchesPmtExpr2: return inputFormatter(matchesPmtExpr2, "pmt")

    matchesPmtExpr3 = re.match("pmt of (-?\d*\.?\d+)", string)
    if matchesPmtExpr3: return inputFormatter(matchesPmtExpr3, "pmt")

    matchesPvExpr1 = re.match("a?\s?present value of (-?\d*\.?\d+)", string)
    if matchesPvExpr1: return inputFormatter(matchesPvExpr1, "pv")

    matchesPvExpr2 = re.match("a?\s?pv = (-?\d*\.?\d+)", string)
    if matchesPvExpr2: return inputFormatter(matchesPvExpr2, "pv")

    matchesPvExpr3 = re.match("a?\s?pv of (-?\d*\.?\d+)", string)
    if matchesPvExpr3: return inputFormatter(matchesPvExpr3, "pv")

    matchesFvExpr1 = re.match("a?\s?future value of (-?\d*\.?\d+)", string)
    if matchesFvExpr1: return inputFormatter(matchesFvExpr1, "fv")

    matchesFvExpr2 = re.match("a?\s?fv = (-?\d*\.?\d+)", string)
    if matchesFvExpr2: return inputFormatter(matchesFvExpr2, "fv")

    matchesFvExpr3 = re.match("a?\s?fv of (-?\d*\.?\d+)", string)
    if matchesFvExpr3: return inputFormatter(matchesFvExpr3, "fv")

    matchesCFExpr1 = re.match("cash flows of (\[-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\])", string.replace("$", ""))
    if matchesCFExpr1: return "cash_flows = " + matchesCFExpr1.group(1).replace("$", "")

    matchesCFExpr2 = re.match("cash flows = (\[-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\])", string.replace("$", ""))
    if matchesCFExpr2: return "cash_flows = " + matchesCFExpr2.group(1).replace("$", "")


    # Currently only works for r and nper. Once all operations have been included (possibly including optional ones), 
    #   throw an error describing the invalid operation.
    else: 
        print("Error: Invalid operation name found. Allowed operations include rate, nper, pmt, pv, fv, and cash flows.")
        return "ERROR: Invalid operation."

def functionParser(string):
    """This function parses the function name into valid Python code."""
    # This statement returns the function name

    matchesNPV = re.match(".*([Nn]et [Pp]resent [Vv]alue|NPV|npv)\?", string)
    if matchesNPV: return "NPV"

    matchesFV = re.match(".*([Ff]uture [Vv]alue|FV|fv)\?", string)
    if matchesFV: return "FV"

    matchesPV = re.match(".*([Pp]resent [Vv]alue|PV|pv)\?", string)
    if matchesPV: return "PV"

    matchesIRR = re.match(".*([Ii]nternal [Rr]ate of [Rr]eturn|IRR|irr)\?", string)
    if matchesIRR: return "IRR"

    else:
        # throw an error
        print("Error: No valid function name found. Allowed function names include: NPV, FV, IRR, and PV.")
        return "Invalid Function Name"

def parse(text):
    """This parses the text into """
    # This splits the text into the two sentences: given and question
    given, question = re.split("\. ", text, maxsplit=1)

    # If the given sentence is not empty, split it into operations
    if given:
        operations = re.split("\,(?![^\[]*\])", given)
        if len(operations) == 1:
            operations = re.split(" and", operations[0])

        # These statements return a list of operations with spaces removed
        inputs = list(map(format_operations1,operations))
        inputs = [ operationParser(input) for input in inputs ]
    
    if question:
        functionName = functionParser(question)

    return inputs, functionName
