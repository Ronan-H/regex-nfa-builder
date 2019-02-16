from nfa import NFA


def get_single_symbol_regex(symbol):
    """ Returns an NFA that recognizes a single symbol """

    nfa = NFA()
    nfa.add_state(1, True)
    nfa.add_transition(0, symbol, 1)

    return nfa


def get_concat(a, b):
    """ Concatenates two NFAs, ie. the dot operator """

    # number to add to each b state number
    # this is to ensure each NFA has separate number ranges for their states
    # one state overlaps; this is the state that connects a and b
    add = max(a.states)

    # update all b states
    new_b_states = set()
    for n in b.states:
        new_b_states.add(n + add)
    b.states = new_b_states

    # update b accept states
    new_b_accept_states = set()
    for n in b.accept_states:
        new_b_accept_states.add(n + add)
    b.accept_states = new_b_accept_states

    # update b transition function
    new_b_transition_function = {}
    for n in b.transition_function:
        new_key = (n[0] + add, n[1])
        new_b_transition_function[new_key] = b.transition_function[n] + add
    b.transition_function = new_b_transition_function

    # merge b into a
    # TODO check if |= operator works as expected (and isn't a bitwise operator etc)
    a.accept_states = b.accept_states
    a.states = a.states | b.states
    a.transition_function.update(b.transition_function)
    a.alphabet = a.alphabet | b.alphabet

    return a


def get_nfa_list_concat(nfa_list):
    if len(nfa_list) == 1:
        return nfa_list[0]

    nfa = nfa_list[0]
    for sub_nfa in nfa_list[1:]:
        nfa = get_concat(nfa, sub_nfa)

    return nfa


def get_regex_nfa(regex):
    """ Recursively builds an NFA based on the given regex """

    # base case: single symbol is directly turned into an NFA
    if len(regex) == 1:
        return get_single_symbol_regex(regex)

    # special symbols: *.| (in order of precedence highest to lowest, symbols coming before that

    # concatenation
    if "." in regex:
        parts = regex.split(".")
        sub_nfa_list = [get_regex_nfa(part) for part in parts]
        return get_nfa_list_concat(sub_nfa_list)
