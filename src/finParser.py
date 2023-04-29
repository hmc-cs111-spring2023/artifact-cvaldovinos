import re

def extractOperations(string):
    """This function removes the 'Given', 'and', and spaces from the start of
        operations."""
    return re.sub("(Given )?(^\s+)?(and )?", "", string)

def inputFormatter(inputs, variable):
    """This function formats the inputs and evaluates any operations within them."""
    operation = list(filter(lambda x: x != None, inputs.groups()))

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

def argumentParser(argument, input):
    string = input.replace("$", "")
    """This function ensures that when one argument is provided that it is provided in a valid format."""
    if argument == "r":
        matchesRateExpr1 = re.match("a?\s?rate of (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
        if matchesRateExpr1: return inputFormatter(matchesRateExpr1, "r")
        
        matchesRateExpr2 = re.match("a?\s?rate\s?=\s?(\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
        if matchesRateExpr2: return inputFormatter(matchesRateExpr2, "r")
            
        matchesRateExpr3 = re.match("a?\s?r\s?=\s?(\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
        if matchesRateExpr3: return inputFormatter(matchesRateExpr3, "r")

        matchesRateExpr4 = re.match("(\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
        if matchesRateExpr4: return inputFormatter(matchesRateExpr4, "r")

    if argument == "cash_flows":
        matchesCFExpr1 = re.match("cash flows of (\[\s?-?\d*\.?\d+(?:,\s?-?\d*\.?\d+)*\s?\])", string)
        if matchesCFExpr1: return "cash_flows = " + matchesCFExpr1.group(1)

        matchesCFExpr2 = re.match("cash flows\s?=\s?(\[\s?-?\d*\.?\d+(?:,\s?-?\d*\.?\d+)*\s?\])", string)
        if matchesCFExpr2: return "cash_flows = " + matchesCFExpr2.group(1)

        matchesCFExpr3 = re.match("cash_flows\s?=\s?(\[\s?-?\d*\.?\d+(?:,\s?-?\d*\.?\d+)*\s?\])", string)
        if matchesCFExpr3: return "cash_flows = " + matchesCFExpr3.group(1)

        matchesCFExpr4 = re.match("(\[\s?-?\d*\.?\d+(?:,\s?-?\d*\.?\d+)*\s?\])", string)
        if matchesCFExpr4: return "cash_flows = " + matchesCFExpr4.group(1)

    if argument == "nper":
        matchesNperExpr1 = re.match("(\d*)(\*\d*)? periods", string)
        if matchesNperExpr1: return inputFormatter(matchesNperExpr1, "nper")

        matchesNperExpr2 = re.match("nper\s?=\s?(\d*)(\*\d*)?", string)
        if matchesNperExpr2: return inputFormatter(matchesNperExpr2, "nper")

        matchesNperExpr3 = re.match("nper of (\d*)(\*\d*)?", string)
        if matchesNperExpr3: return inputFormatter(matchesNperExpr3, "nper")

        matchesNperExpr4 = re.match("(\d*)(\*\d*)?", string)
        if matchesNperExpr4: return inputFormatter(matchesNperExpr4, "nper")

    if argument == "pmt":
        matchesPmtExpr1 = re.match("\$-(\d*\.?\d+) payments", input)
        if matchesPmtExpr1: return "pmt = " + matchesPmtExpr1.group(1)

        matchesPmtExpr2 = re.match("\$(\d*\.?\d+) payments", input)
        if matchesPmtExpr2: return "pmt = -" + matchesPmtExpr2.group(1)

        matchesPmtExpr3 = re.match("pmt\s?=\s?\$?(-?\d*\.?\d+)", input)
        if matchesPmtExpr3: return "pmt = " + matchesPmtExpr3.group(1)

        matchesPmtExpr4 = re.match("pmt of \$?(-?\d*\.?\d+)", input)
        if matchesPmtExpr4: return "pmt = " + matchesPmtExpr4.group(1)

        matchesPmtExpr5 = re.match("\$?(-?\d*\.?\d+)", input)
        if matchesPmtExpr5: return "pmt = " + matchesPmtExpr5.group(1)

    if argument == "pv":
        matchesPVExpr1 = re.match("a?\s?present value of (-?\d*\.?\d+)", string)
        if matchesPVExpr1: return "pv = " + matchesPVExpr1.group(1)

        matchesPVExpr2 = re.match("a?\s?pv\s?=\s?(-?\d*\.?\d+)", string)
        if matchesPVExpr2: return "pv = " + matchesPVExpr2.group(1)

        matchesPVExpr3 = re.match("a?\s?pv of (-?\d*\.?\d+)", string)
        if matchesPVExpr3: return "pv = " + matchesPVExpr3.group(1)

        matchesPVExpr4 = re.match("(-?\d*\.?\d+)", string)
        if matchesPVExpr4: return "pv = " + matchesPVExpr4.group(1)

    if argument == "fv":
        matchesFVExpr1 = re.match("a?\s?future value of (-?\d*\.?\d+)", string)
        if matchesFVExpr1: return "fv = " + matchesFVExpr1.group(1)

        matchesFVExpr2 = re.match("a?\s?fv\s?=\s?(-?\d*\.?\d+)", string)
        if matchesFVExpr2: return "fv = " + matchesFVExpr2.group(1)

        matchesFVExpr3 = re.match("a?\s?fv of (-?\d*\.?\d+)", string)
        if matchesFVExpr3: return "fv = " + matchesFVExpr3.group(1)

        matchesFVExpr4 = re.match("(-?\d*\.?\d+)", string)
        if matchesFVExpr4: return "fv = " + matchesFVExpr4.group(1)

    return "Invalid argument."

def operationParser(input):
    """This function parses the input string and returns the inputs and the function name."""
    string = input.replace("$", "")

    matchesRateExpr1 = re.match("a?\s?rate of (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr1: return inputFormatter(matchesRateExpr1, "r")

    matchesRateExpr2 = re.match("a?\s?rate\s?=\s?(\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr2: return inputFormatter(matchesRateExpr2, "r")
        
    matchesRateExpr3 = re.match("a?\s?r\s?=\s?(\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr3: return inputFormatter(matchesRateExpr3, "r")

    matchesNperExpr1 = re.match("(\d*)(\*\d*)? periods", string)
    if matchesNperExpr1: return inputFormatter(matchesNperExpr1, "nper")

    matchesNperExpr2 = re.match("nper\s?=\s?(\d*)(\*\d*)?", string)
    if matchesNperExpr2: return inputFormatter(matchesNperExpr2, "nper")

    matchesNperExpr3 = re.match("nper of (\d*)(\*\d*)?", string)
    if matchesNperExpr3: return inputFormatter(matchesNperExpr3, "nper")

    # We do not replace the $ here because $100 payments is different than 100 payments (pmt = -100 vs. nper = 100).
    matchesPmtExpr1 = re.match("\$-(\d*\.?\d+) payments", input)
    if matchesPmtExpr1: return "pmt = " + matchesPmtExpr1.group(1)

    matchesPmtExpr2 = re.match("\$(\d*\.?\d+) payments", input)
    if matchesPmtExpr2: return "pmt = -" + matchesPmtExpr2.group(1)

    matchesPmtExpr3 = re.match("pmt\s?=\s?(-?\d*\.?\d+)", string)
    if matchesPmtExpr3: return inputFormatter(matchesPmtExpr3, "pmt")

    matchesPmtExpr4 = re.match("pmt of (-?\d*\.?\d+)", string)
    if matchesPmtExpr4: return inputFormatter(matchesPmtExpr4, "pmt")

    matchesPvExpr1 = re.match("a?\s?present value of (-?\d*\.?\d+)", string)
    if matchesPvExpr1: return inputFormatter(matchesPvExpr1, "pv")

    matchesPvExpr2 = re.match("a?\s?pv\s?=\s?(-?\d*\.?\d+)", string)
    if matchesPvExpr2: return inputFormatter(matchesPvExpr2, "pv")

    matchesPvExpr3 = re.match("a?\s?pv of (-?\d*\.?\d+)", string)
    if matchesPvExpr3: return inputFormatter(matchesPvExpr3, "pv")

    matchesFvExpr1 = re.match("a?\s?future value of (-?\d*\.?\d+)", string)
    if matchesFvExpr1: return inputFormatter(matchesFvExpr1, "fv")

    matchesFvExpr2 = re.match("a?\s?fv\s?=\s?(-?\d*\.?\d+)", string)
    if matchesFvExpr2: return inputFormatter(matchesFvExpr2, "fv")

    matchesFvExpr3 = re.match("a?\s?fv of (-?\d*\.?\d+)", string)
    if matchesFvExpr3: return inputFormatter(matchesFvExpr3, "fv")

    matchesCfExpr1 = re.match("cash flows of (\[\s*-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s*\])", string)
    if matchesCfExpr1: return "cash_flows = " + matchesCfExpr1.group(1)

    matchesCfExpr2 = re.match("cash flows\s?=\s?(\[\s*-?\d*\.?\d+(?:,\s*-?\d*\.?\d+)*\s*\])", string)
    if matchesCfExpr2: return "cash_flows = " + matchesCfExpr2.group(1)

    else: 
        print("\nERROR: Invalid input found: " + string + "\n\nAllowed inputs include rate, nper, pmt, pv, fv, and cash flows.")
        return "ERROR: Invalid input."

def functionParser(string):
    """This function parses the second sentence and returns the function name."""

    matchesNPV = re.match(".*([Nn]et [Pp]resent [Vv]alue|NPV|npv)\?", string)
    if matchesNPV: return "NPV"

    matchesFV = re.match(".*([Ff]uture [Vv]alue|FV|fv)\?", string)
    if matchesFV: return "FV"

    matchesPV = re.match(".*([Pp]resent [Vv]alue|PV|pv)\?", string)
    if matchesPV: return "PV"

    matchesIRR = re.match(".*([Ii]nternal [Rr]ate of [Rr]eturn|IRR|irr)\?", string)
    if matchesIRR: return "IRR"

    else:
        return "Invalid Function Name"

def parse(text):
    """This function parses the input text and returns the inputs and the function name."""
    match = re.match("Given\s(.*)\. What is (.*)\?", text)
    if match:
        # This splits the text into the two sentences: given and question
        given, question = re.split("\. ", text, maxsplit=1)

        # This splits the given inputs into a list of operations
        operations = re.split("\,(?![^\[]*\])", given)
        if len(operations) == 1:
            operations = re.split(" and", operations[0])

        # These statements return a list of operations with spaces removed
        inputs = list(map(extractOperations,operations))
        inputs = [ operationParser(input) for input in inputs ]
    
        # This statement returns the function name
        functionName = functionParser(question)

        return inputs, functionName

    else:
        print("\nERROR: Invalid input.\n\nA valid input must be of the format:\n\tGiven <input>, <input>," + 
                  " and <input>. What is <function name>?\n")
        return None, None
