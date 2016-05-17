from  Luis import Luis
from Action import Action, ActionList


class Brain:
    def __init__(self):
        self.luis = Luis()
        self.acter = Action()
        self.initialize()

    def initialize(self):
        self.luis.initialize()

    def intent_to_action(self, intent):
        if intent == 'Learn':
            return ActionList.Clarify

        if intent == 'quit':
            return ActionList.Quit

        return ActionList.DidNotUnderstand

    def Chat(self):
        keep_chatting = True
        print 'Type your question here. Type "quit" to quit'
        while keep_chatting:
            user_sentence = raw_input('You:')
            intent, topic = self.luis.get_intent_and_entity(user_sentence)
            action = self.intent_to_action(intent)
            print self.acter.act(action, topic, keep_chatting)
