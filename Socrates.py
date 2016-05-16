from Brain import Brain


class Socrates:
    def __init__(self):
        self.brain = Brain()

    def Initialize(self):
        self.brain.initialize()

    def ask(self, question):
        return self.brain.process_input(question)

    def Chat(self):
        keep_chatting = True
        print 'Type your question here. Type "quit" to quit'
        while keep_chatting:
            question = raw_input('You:')
            print self.ask(question)
            if question == 'quit':
                keep_chatting = False


if __name__ == '__main__':
    bot = Socrates()
    bot.Initialize()
    bot.Chat()
