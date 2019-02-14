import unittest
from nfa import NFA


class TestNFA(unittest.TestCase):
    def test_transition(self):
        nfa = NFA("")
        nfa.add_state(1, True)
        nfa.add_transition(0, "a", 1)

        self.assertFalse(nfa.is_accepting())
        nfa.feed_symbol("a")
        self.assertTrue(nfa.is_accepting())
        nfa.feed_symbol("a")
        self.assertFalse(nfa.is_accepting())

