import os
import sys
import json

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote

class Translate(object):
    base_url = 'https://openapi.naver.com/v1'

    def __init__(self, client_id, secret):
        self.headers = {
            'X-Naver-Client-Id': '{}'.format(client_id),
            'X-Naver-Client-Secret': '{}'.format(secret)
        }

    def nmt_translate_kr_en(self, text):
        req = Request(url='{}/papago/n2mt'.format(self.base_url),\
                      headers = self.headers)
        data = 'source=ko&target=en&text=' + quote(text)
        response = urlopen(req, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode==200):
            content = json.loads(response.read().decode('utf-8'))
            translated_text = content.get('message')['result']\
                                         ['translatedText']
            return translated_text
        else:
            return 'Error: {}'.format(response.getcode())

    def nmt_translate_en_kr(self, text):
        req = Request(url='{}/papago/n2mt'.format(self.base_url),\
                      headers = self.headers)
        data = 'source=en&target=ko&text=' + quote(text)
        response = urlopen(req, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode==200):
            content = json.loads(response.read().decode('utf-8'))
            translated_text = content.get('message')['result']\
                                         ['translatedText']
            return translated_text
        else:
            return 'Error: {}'.format(response.getcode())