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
        if intent.lower() == 'learn':
            return ActionList.Clarify

        if intent.lower() == 'quit':
            return ActionList.Quit

        return ActionList.DidNotUnderstand

    def Chat(self):
        keep_chatting = True
        print 'Type your question here. Type "quit" to quit'
        while keep_chatting:
            user_sentence = raw_input('You:')
            intent, topic = self.luis.get_intent_and_entity(user_sentence)
            action = self.intent_to_action(intent)
            print self.acter.act(action, topic)
            if action == ActionList.Quit:
                keep_chatting = False
