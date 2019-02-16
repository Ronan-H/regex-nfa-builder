import unittest
import nfa_utils


class TestNFA(unittest.TestCase):

    def test_single_symbol_nfa(self):
        print("Testing single symbol regex NFA")

        nfa = nfa_utils.get_single_symbol_regex("x")
        print(nfa)

        # test NFA state
        self.assertEqual(nfa.alphabet,{'x'})
        self.assertEqual(nfa.states, {0, 1})
        self.assertEqual(nfa.transition_function, {(0, 'x'): 1})
        self.assertEqual(nfa.accept_states, {1})
        self.assertEqual(nfa.in_states, {0})

        # test NFA behaviour
        self.assertFalse(nfa.is_accepting())

        nfa.feed_symbol("x")
        self.assertEqual(nfa.in_states, {1})
        self.assertTrue(nfa.is_accepting())

        nfa.feed_symbol("x")
        self.assertFalse(nfa.is_accepting())
        self.assertEqual(nfa.in_states, set())
        self.assertTrue(nfa.is_dead())

    def test_nfa_concat(self):
        print("Testing concatenated NFA a.b")

        # recognizes "a.b"
        nfa = nfa_utils.get_concat(nfa_utils.get_single_symbol_regex("a"),
                                   nfa_utils.get_single_symbol_regex("b"))
        print(nfa)

        self.assertFalse(nfa.is_accepting())
        nfa.feed_symbol("a")
        self.assertFalse(nfa.is_accepting())
        nfa.feed_symbol("b")
        self.assertTrue(nfa.is_accepting())
        nfa.feed_symbol("a")
        self.assertFalse(nfa.is_accepting())

    def test_big_nfa_concat(self):
        print("Testing concatenated NFA a.b.c.c.b.a.G.G.G")

        concat_strings = ["abc", "cba", "GGG"]

        # construct a large NFA by creating 3 sub NFAs, and
        # concatenating them together
        nfa = None
        for str in concat_strings:
            # construct sub nfa
            sub_nfa = None
            for c in str:
                if sub_nfa is None:
                    sub_nfa = nfa_utils.get_single_symbol_regex(c)
                else:
                    sub_nfa = nfa_utils.get_concat(sub_nfa, nfa_utils.get_single_symbol_regex(c))

            # combine this sub NFA with the overall NFA
            if nfa is None:
                nfa = sub_nfa
            else:
                nfa = nfa_utils.get_concat(nfa, sub_nfa)

        print(nfa)

        # ensure the NFA does not accept until the entire input string has been fed in
        input_str = "".join(concat_strings)

        for symbol in input_str:
            self.assertFalse(nfa.is_accepting())
            nfa.feed_symbol(symbol)

        self.assertTrue(nfa.is_accepting())

    def test_empty_string(self):
        print("Testing empty string transitions")

        # construct an NFA equivalent to a|<empty string>
        nfa = nfa_utils.get_single_symbol_regex("a")
        nfa.add_state(2, True)
        nfa.add_transition(0, "", 2)
        nfa.reset()
        print(nfa)

        # NFA should accept straight away due to the emoty string transition
        # from the initial state to an acecpt state
        self.assertTrue(nfa.is_accepting())
        # after feeding an 'a', the NFA should accept; state 2 is dead
        # but a transition from state 0 to 1 (accepts) should still work
        nfa.feed_symbol("a")
        self.assertTrue(nfa.is_accepting())
        # after feeding a final a, the NFA should be dead (no transitions available
        # for the current "active" states)
        nfa.feed_symbol("a")
        self.assertFalse(nfa.is_accepting())
        self.assertTrue(nfa.is_dead())