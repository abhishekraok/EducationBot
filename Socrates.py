from Brain import Brain


class Socrates:
    def __init__(self):
        self.brain = Brain()

    def Chat(self):
        self.brain.Chat()


if __name__ == '__main__':
    bot = Socrates()
    bot.Chat()
