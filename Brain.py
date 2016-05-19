from Action import Action
from  Luis import Luis
from State import State, StateCollection


class Brain:
    def __init__(self):
        self.luis = Luis()
        self.luis.initialize()
        self.acter = Action()
        self.state_manager = StateCollection()
        self.state_manager.load('states.json')
        self.current_state = self.state_manager.starting_state()
        with open('txt/intro.txt', 'r') as f:
            self.help_message = f.read()

    def step(self):
        result = self.acter.act_state(self.current_state)
        self.current_state = self.current_state.next_state(result)

    # def intent_to_state(self, intent):
    #     self.current_state = self.current_state.next_state(intent)
    #
    # def intent_to_action(self, intent):
    #     if intent.lower() == 'learn':
    #         return ActionList.Clarify
    #
    #     if intent.lower() == 'quit':
    #         return ActionList.Quit
    #
    #     return ActionList.DidNotUnderstand

    def Chat(self):
        keep_chatting = True
        print self.help_message
        while keep_chatting:
            user_sentence = raw_input('You:')
            intent, topic = self.luis.get_intent_and_entity(user_sentence)
            self.step()
            if self.current_state == 'quit':
                keep_chatting = False
