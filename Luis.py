import httplib
import urllib
import json

class Luis:
    def __init__(self):
        self.appid = ''
        self.subscriptionkey = ''

    def initialize(self):
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
            return self.decode_json(data)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            return 0

    def decode_json(self, luis_reply):
        return json.loads(luis_reply)
