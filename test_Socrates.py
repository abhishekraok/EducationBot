import unittest
from Socrates import Socrates
from State import StateCollection, State


class TestSocrates(unittest.TestCase):
    def test_I_want_to_learn_about_mars_reply_greater_than_0(self):
        question = "I want to learn about mars"
        bot = Socrates()
        reply = bot.brain.ask(question)
        self.assertGreater(len(reply), 20)

    def test_StateCollection_loads(self):
        states = StateCollection()
        states.load('test_states.json')
        self.assertTrue(len(states.states) > 0)

    def test_StateCollection_first_state(self):
        states = StateCollection()
        states.load('test_states.json')
        self.assertEqual(states.states['first_state'].state_name, 'first_state')

if __name__ == '__main__':
    unittest.main()
