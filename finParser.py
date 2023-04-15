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
    operation = list(filter(lambda x: x != None, match.groups()))
    if (len(operation) == 2):
        return variable + " = " + operation[0] + operation[1]
    else:
        return variable + " = " + operation[0]

def operationParser(string):
    """This function parses the operations into valid Python code."""

    matchesRateExpr1 = re.match("a rate of (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr1: return inputFormatter(matchesRateExpr1, "r")

    matchesRateExpr2 = re.match("rate = (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr2: return inputFormatter(matchesRateExpr2, "r")
        
    matchesRateExpr3 = re.match("r = (\d*.?\d*\%?)(\/\d*|\*\d*)?", string)
    if matchesRateExpr3: return inputFormatter(matchesRateExpr3, "r")

    matchesNPERExpr1 = re.match("(\d*)(\*\d*)? periods", string)
    if matchesNPERExpr1: return inputFormatter(matchesNPERExpr1, "nper")

    matchesNPERExpr2 = re.match("nper = (\d*)(\*\d*)?", string)
    if matchesNPERExpr2: return inputFormatter(matchesNPERExpr2, "nper")

    matchesNPERExpr3 = re.match("nper of (\d*)(\*\d*)?", string)
    if matchesNPERExpr3: return inputFormatter(matchesNPERExpr3, "nper")

    # Currently only works for r and nper. Once all operations have been included (possibly including optional ones), 
    #   throw an error describing the invalid operation.
    else: return string

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

