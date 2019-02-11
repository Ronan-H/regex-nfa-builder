import sys


class NFA:
    """class representing a non-deterministic finite automaton"""

    def __init__(self, regex):
        self.states = set()
        self.alphabet = set(regex)
        self.transition_function = {}
        self.start_state = 0
        self.accept_states = set()

        # set of states that the NFA is currently in
        self.in_states = set()

        print("Alphabet: ", self.alphabet)

    def add_state(self, state):
        self.states += state

    def add_transition(self, from_state, symbol, to_state):
        self.transition_function[(from_state, symbol)] = to_state

    def feed_symbol(self, symbol):
        # feeds a symbol into the NFA, calculating which states the
        # NFA is now in, based on which states it used to be in

        new_states = set()

        # process each old state in turn
        for state in self.states:
            pair = (state, symbol)

            # check for a legal transition from the old state to a
            # new state, based on what symbol was fed in
            if pair in self.states:
                # add the corresponding new state to the updated states list
                new_states.add(self.transition_function[pair])

        self.states = new_states

    def is_accepting(self):
        # accepts if we are in ANY accept states
        # ie. accepts if in_states and accept_states share any states in common
        return len(self.in_states & self.accept_states) > 0


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
