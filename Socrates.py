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
        # params = urllib.urlencode({'q':question})
        quoted_question = urllib.quote(question)
        try:
            url = 'https://api.projectoxford.ai/luis/v1/application/'
            # values = {
            #     'id': self.appid,
            #     'subscription-key': self.subscriptionkey,
            #     'q': question,
            # }
            # data = urllib.urlencode(values)
            # req = urllib2.Request(url, data)
            # response = urllib2.urlopen(req)

            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            query = '/luis/v1/application?id=' + self.appid + '&subscription-key=' + self.subscriptionkey + '&q=' + quoted_question
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


if __name__ == '__main__':
    bot = Socrates()
    bot.Initialize()
    reply = bot.ask("I want to learn about Electrostatics")
    print reply
