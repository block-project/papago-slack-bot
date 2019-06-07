# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from .nmt import Translate

class Bot(BaseBot):

    @channel()
    def default_handler(self, event, context):

        message = event.get('content')
        flag = self.isEnglishOrKorean(message)
        self.translate_message(message, flag)


    def translate_message(self, text, flag):
        client_id = self.get_project_data()['client_id']
        secret = self.get_project_data()['secret']
        t = Translate(client_id, secret)
        if flag == 0:
            msg = t.nmt_translate_kr_en(text)
        else:
            msg = t.nmt_translate_en_kr(text)
        self.send_message(msg)


    def isEnglishOrKorean(self, input_s):
        k_count = 0
        e_count = 0
        for c in input_s:
            if ord('가') <= ord(c) <= ord('힣'):
                k_count+=1
            elif ord('a') <= ord(c.lower()) <= ord('z'):
                e_count+=1
        return 0 if k_count>1 else 1

