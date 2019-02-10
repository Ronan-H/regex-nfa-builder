
print("\n== Regex NFA Builder by Ronan Hanley ==\n")

print("Set the regular expression by typing regex=(regex here)")
print("Example: regex=011010\n")

print("You can give input text to test against that regex by just typing it in by itself.\n")

# regular expression string to compare against provided input
regex = None
line_read = None

while line_read != "exit":
    line_read = input("> ")

    if line_read.startswith("regex="):
        regex = line_read[6:]
        print("New regex string:", regex)
    else:
        if regex is None:
            print("Please supply a regular expression string first")
        else:
            print("(Matching test done here)")

    print()
