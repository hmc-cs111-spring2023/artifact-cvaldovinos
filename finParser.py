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

def parse(text):
    """This parses the text into """
    # This splits the text into the two sentences: given and question
    given, question = re.split("\. ", text, maxsplit=1)
    # if given: return (given, question)
    # print(given)

    # If the given sentence is not empty, split it into operations
    if given:
        operations = re.split("\,(?![^\[]*\])", given)
        if len(operations) == 1:
            operations = re.split(" and", operations[0])

        if (len(operations) != 2):
            inputs = list(map(format_operations1,operations))
            # print("Inputs:       ", list(map(format_operations,operations)))
        # Returns a list of operations with spaces removed
        else:
            inputs = list(map(format_operations1,operations))
            # print("Inputs:       ", list(map(format_operations1,operations)))
    
    if question:
        func = re.match(".*([Nn]et [Pp]resent [Vv]alue|NPV|npv|[Ff]uture [Vv]alue|FV|fv|[Ii]nternal [Rr]ate of [Rr]eturn|IRR|irr)\?", question)
        if func: functionName = func.groups()[0]
        else:
            func = re.match(".*([Pp]resent [Vv]alue|PV|pv)\?", question)
            functionName = func.groups()[0]
        # Returns the function name
        # functionName = func.groups()[0]
        # print("Function name: ", func)
    
    return inputs, functionName

