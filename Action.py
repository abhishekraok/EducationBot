#
# class ActionList(Enum):
#     AskQuestion = 0,
#     Clarify = 1,
#     DidNotUnderstand = 2,
#     Quit = 3
from Result import Result


class Action():
    @staticmethod
    def say(words):
        print 'Socrates: ' + words

    # def act(self, action, topic):
    #
    #     if (action == ActionList.AskQuestion):
    #         return "What is " + topic + "?"
    #
    #     if (action == ActionList.Clarify):
    #         try:
    #             return wikipedia.summary(topic)
    #         except wikipedia.exceptions.WikipediaException as w:
    #             return "Did not find article in Wikipedia for " + w.message
    #
    #     if (action == ActionList.DidNotUnderstand):
    #         return "Sorry I did not understand what " + topic + " means."
    #
    #     if (action == ActionList.Quit):
    #         return "Goodbye"

    def act_state(self, current_state):
        result = getattr(StateFunctions, current_state)()
        return result

    @classmethod
    def listen(cls):
        user_reply = raw_input('You:')
        return user_reply


class StateFunctions():
    @staticmethod
    def start():
        reply = 'Starting Socrates Bot'
        Action.say(reply)
        return Result(True, reply, '')

    @staticmethod
    def greet():
        reply = 'Hello, nice to meet you'
        Action.say(reply)
        return Result(True, reply , '')

    @staticmethod
    def choose_topic():
        reply = 'What do you want to learn today?'
        Action.say(reply)
        user_reply = Action.listen()
        Action.say('OK so you want to learn about ' + user_reply)
        return Result(True, user_reply, '')

    @staticmethod
    def first_state():
        return Result(True, '', '')

    @staticmethod
    def second_state():
        return Result(True, '', '')

    @staticmethod
    def quit():
        Action.say('Bye bye')
        return Result(True, '', '')