from  Luis import Luis
from Action import Action, ActionList


class Brain:
    def __init__(self):
        self.luis = Luis()
        self.acter = Action()

    def initialize(self):
        self.luis.initialize()

    def process_input(self, user_sentence):
        intent, topic = self.luis.query(user_sentence)
        action = self.intent_to_action(intent)
        return self.acter.act(action, topic)

    def intent_to_action(self, intent):
        if intent == 'learn':
            return ActionList.AskQuestion
