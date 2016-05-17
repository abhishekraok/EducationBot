from  Luis import Luis
from Action import Action, ActionList


class Brain:
    def __init__(self):
        self.luis = Luis()
        self.acter = Action()
        self.initialize()

    def initialize(self):
        self.luis.initialize()

    def process_input(self, user_sentence):
        intent, topic = self.luis.get_intent_and_entity(user_sentence)
        action = self.intent_to_action(intent)
        return self.acter.act(action, topic)

    def intent_to_action(self, intent):
        if intent == 'Learn':
            return ActionList.Clarify

        if intent == 'quit':
            return ActionList.Quit

        return ActionList.DidNotUnderstand
