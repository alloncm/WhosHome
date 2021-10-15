from io import StringIO
from typing import Text
from telegram.ext import Updater, CommandHandler
import nmap_scanner
import config

class TelegramUi:
    def __init__(self, token:str) -> None:
        self.updater = Updater(token=token,use_context=True)
        self.dipatcher = self.updater.dispatcher

        whos_home_handler = CommandHandler('whoshome', self.whos_home_callback)
        self.dipatcher.add_handler(whos_home_handler)
    
    def whos_home_callback(self, update, context):
        if update.effective_chat.id not in config.ALLOWED_IDS:
            context.bot.send_message(chat_id=update.effective_chat.id, text='You are not allowed to use this bot, fuck off!')
            return
        message = 'processing...'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        scan_output = nmap_scanner.scan_host_on_network()

        output_buffer = StringIO()

        if len(context.args) == 1 and 'raw' in context.args:
            for device in scan_output:
                device_raw = 'ip:' + device.ip + ' hn:' + device.hostname + ' mac origin:' + device.mac_origin + ' mac:' + device.mac + '\n'
                output_buffer.write(device_raw)
        else:
            output_buffer.write('Members found are: \n')
            for device in scan_output:
                if device.mac in config.MAC_MEMBER_MAPPING:
                    output_buffer.write(config.MAC_MEMBER_MAPPING[device.mac])
                    output_buffer.write('\n')

        context.bot.send_message(chat_id=update.effective_chat.id, text=output_buffer.getvalue())

    def start_bot(self):
        self.updater.start_polling()