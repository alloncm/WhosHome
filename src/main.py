from telegram_ui import TelegramUi
from config import TELEGRAM_TOKEN

telui = TelegramUi(TELEGRAM_TOKEN)
print('Started bot')
telui.start_bot()