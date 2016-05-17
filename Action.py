from enum import Enum
import wikipedia


class ActionList(Enum):
    AskQuestion = 0,
    Clarify = 1,
    DidNotUnderstand = 2,
    Quit = 3


class Action():
    def act(self, action, topic, keep_chatting):

        if (action == ActionList.AskQuestion):
            return "What is " + topic + "?"

        if (action == ActionList.Clarify):
            return wikipedia.summary(topic)

        if (action == ActionList.DidNotUnderstand):
            return "Sorry I did not understand what " + topic + "means."

        if (action == ActionList.Quit):
            keep_chatting = False
            return "Goodbye"
