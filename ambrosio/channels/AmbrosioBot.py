

import telepot


class AmbrosioBot(telepot.Bot):
    """AmbrosioBot is my telegram bot"""
    def __init__(self, token):
        super(AmbrosioBot, self).__init__(token)
        self.clist = None

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if self.clist is not None:
                self.clist.append(command)
