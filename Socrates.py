import httplib, urllib, base64
import urllib2


class Luis:
    def __init__(self):
        self.appid = ''
        self.subscriptionkey = ''

    def Initialize(self):
        with open('key.txt', 'r') as f:
            file_content = f.read().strip().split('\n')
            self.appid, self.subscriptionkey = file_content
        self.headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.subscriptionkey,
        }

    def query(self, question):
        quoted_question = urllib.quote(question)
        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            query = '/luis/v1/application?id=' + self.appid + '&subscription-key=' \
                    + self.subscriptionkey + '&q=' + quoted_question
            conn.request("POST", query, "{body}", self.headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return data
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


class Socrates:
    def __init__(self):
        self.luis = Luis()

    def Initialize(self):
        self.luis.Initialize()

    def ask(self, question):
        return self.luis.query(question)

    def Chat(self):
        keep_chatting = True
        print 'Type your question here. Type "quit" to quit'
        while keep_chatting:
            question = input('You:')
            print self.ask(question)
            if question == 'quit':
                keep_chatting = False


if __name__ == '__main__':
    bot = Socrates()
    bot.Initialize()
    bot.Chat()
