import unittest
from Socrates import Socrates


class TestSocrates(unittest.TestCase):
    def test_I_want_to_learn_about_mars_reply_greater_than_0(self):
        question = "I want to learn about mars"
        bot = Socrates()
        reply = bot.brain.ask(question)
        self.assertGreater(len(reply), 20)


if __name__ == '__main__':
    unittest.main()
