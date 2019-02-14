import sys
from nfa import NFA

# print the welcome text block
# TODO: read this from a file instead?
print("\n== Regex NFA Builder by Ronan Hanley ==\n")

print("Set the regular expression by typing regex=(regex here)")
print("Example: regex=011010\n")

print("You can give input text to test against that regex by just typing it in by itself.\n")

# regular expression string to compare against provided input
regex = None
# last line of user input read from the command line
line_read = ""

# continuously parse and process user input
while True:
    # read in line of user input
    line_read = input("> ")
    # make a lowercase copy of the input for case insensitive comparisons
    line_read_lower = line_read.lower()

    if line_read_lower == "exit":
        # exit the program
        print("\nExiting...")
        sys.exit()

    if line_read_lower.startswith("regex="):
        # user wants to set the regex to a string they've provided
        regex = line_read[6:]
        print("New regex string:", regex)
        NFA(regex)
    else:
        # assume the user intends to test this entered string against the regex
        if regex is None:
            # regex has not yet been set
            print("Please supply a regular expression string first")
        else:
            print("(Regex matching test done here)")

    # print a new line for aesthetics
    print()
