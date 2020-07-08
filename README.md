# Telegram Notifier
This package provides simple notifications from your app to your Telegram chat
## Preparation:
- Create bot with BotFather and copy the `token`
- Send any message to the bot (needed to automatically get `chat_id`)
- install module:
```bash
pip install telegram-notifier
```
## Usage:
```python
from telegram_notifier import TelegramNotifier
import os
token = os.environ.get("TELEGRAM_TOKEN")
notifier = TelegramNotifier(token, parse_mode="HTML")
notifier.send("<b>Test bold text</b> and normal text")
```
