class NFA:
    """class representing a non-deterministic finite automaton"""

    def __init__(self, regex):
        # all NFAs have a single initial state by default
        self.states = {0}
        self.alphabet = set(regex)
        self.transition_function = {}
        self.accept_states = set()

        # set of states that the NFA is currently in
        self.in_states = self.states.copy()

        print("Alphabet: ", self.alphabet)

    def add_state(self, state, accepts=False):
        self.states.add(state)

        if accepts:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        self.transition_function[(from_state, symbol)] = to_state

    def feed_symbol(self, symbol):
        # feeds a symbol into the NFA, calculating which states the
        # NFA is now in, based on which states it used to be in

        new_states = set()

        # process each old state in turn
        for state in self.in_states:
            pair = (state, symbol)

            # check for a legal transition from the old state to a
            # new state, based on what symbol was fed in
            if pair in self.transition_function:
                # add the corresponding new state to the updated states list
                new_states.add(self.transition_function[pair])

        self.in_states = new_states

    def is_accepting(self):
        # accepts if we are in ANY accept states
        # ie. accepts if in_states and accept_states share any states in common
        return len(self.in_states & self.accept_states) > 0

