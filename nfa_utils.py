from nfa import NFA

def get_single_symbol_regex(symbol):
    nfa = NFA()
    nfa.add_state(1, True)
    nfa.add_transition(0, symbol, 1)

    return nfa

def get_concat(a, b):
    add = max(a.states) + 1

    new_b_states = set()
    for n in b.states:
        new_b_states.add(n + add)
    b.states = new_b_states
    new_b_accept_states = set()
    for n in b.accept_states:
        new_b_accept_states.add(n + add)

    a.accept_states = b.accept_states
    a.states = a.states | b.states
    a.update(b)
    a.alphabet = a.alphabet | b.alphabet

    return a


def get_regex_nfa(regex):
    if len(regex) == 1:
        return get_single_symbol_regex(regex)

    # special symbols: .|&*
