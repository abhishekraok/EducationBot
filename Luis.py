import urllib2
import urllib
import json

class Luis:
    def __init__(self):
        self.appid = ''
        self.subscriptionkey = ''
        self.initialize()

    def initialize(self):
        with open('key.txt', 'r') as f:
            file_content = f.read().strip().split('\n')
            self.appid, self.subscriptionkey = file_content
        self.headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.subscriptionkey,
        }

    def get_intent_and_entity(self, question):
        quoted_question = urllib.quote(question)

        try:
            url_luis = 'https://api.projectoxford.ai/luis/v1/application?id=' + self.appid + '&subscription-key=' \
                    + self.subscriptionkey + '&q=' + quoted_question
            response = urllib2.urlopen(url_luis)
            json = response.read()
            return self.decode_json(json)

        except Exception as e:
            print 'Error ', e.message
            return 'quit', ''

    def decode_json(self, luis_reply):
        luis_full = json.loads(luis_reply)
        intent = luis_full['intents'][0]['intent']
        entity = luis_full['entities'][0]['entity'] if len(luis_full['entities']) > 0 else ''
        return intent, entity
