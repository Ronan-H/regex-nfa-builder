from nfa import NFA


def get_single_symbol_regex(symbol):
    """ Returns an NFA that recognizes a single symbol """

    nfa = NFA()
    nfa.add_state(1, True)
    nfa.add_transition(0, symbol, {1})

    return nfa


def shift(nfa, inc):
    """
    Increases the value of all states (including accept states and transition function etc)
    of a given NFA bya given value.

    This is useful for merging NFAs, to prevent overlapping states
    """
    # update NFA states
    new_states = set()
    for state in nfa.states:
        new_states.add(state + inc)
    nfa.states = new_states

    # update NFA accept states
    new_accept_states = set()
    for state in nfa.accept_states:
        new_accept_states.add(state + inc)
    nfa.accept_states = new_accept_states

    # update NFA transition function
    new_transition_function = {}
    for pair in nfa.transition_function:
        to_set = nfa.transition_function[pair]
        new_to_set = set()

        for state in to_set:
            new_to_set.add(state + inc)

        new_key = (pair[0] + inc, pair[1])
        new_transition_function[new_key] = new_to_set

    nfa.transition_function = new_transition_function


def merge(a, b):
    """Merges two NFAs into one by combining their states and transition function"""
    a.accept_states = b.accept_states
    a.states |= b.states
    a.transition_function.update(b.transition_function)
    a.alphabet |= b.alphabet


def get_concat(a, b):
    """ Concatenates two NFAs, ie. the dot operator """

    # number to add to each b state number
    # this is to ensure each NFA has separate number ranges for their states
    # one state overlaps; this is the state that connects a and b
    add = max(a.states)

    # shift b's state/accept states/transition function, etc.
    shift(b, add)

    # merge b into a
    merge(a, b)

    return a


def get_nfa_list_concat(nfa_list):
    """
    Concatenates a list of NFA objects into one nfa

    Eg. The NFA list [a, b, c] become a single NFA a.b.c
    """

    if len(nfa_list) == 1:
        return nfa_list[0]

    nfa = nfa_list[0]
    for sub_nfa in nfa_list[1:]:
        nfa = get_concat(nfa, sub_nfa)

    return nfa


def get_union(a, b):
    """Returns the resulting union of two NFAs.(the '|' operator)"""

    nfa = NFA()

    a.accept_states = set()
    b.accept_states = set()

    shift(a, 1)
    merge(nfa, a)

    shift(b, max(nfa.states) + 1)
    merge(nfa, b)

    nfa.add_transition(0, "", {1, min(b.states)})

    new_accept = max(nfa.states) + 1
    nfa.add_state(new_accept, True)
    nfa.add_transition(max(a.states), "", {new_accept})
    nfa.add_transition(max(b.states), "", {new_accept})

    nfa.reset()

    return nfa


def get_regex_nfa(regex):
    """Recursively builds an NFA based on the given regex string"""

    # base case: single symbol is directly turned into an NFA
    if len(regex) == 1:
        return get_single_symbol_regex(regex)

    # special symbols: *.| (in order of precedence highest to lowest, symbols coming before that

    # concatenation operator
    if "." in regex:
        parts = regex.split(".")
        sub_nfa_list = [get_regex_nfa(part) for part in parts]
        return get_nfa_list_concat(sub_nfa_list)

