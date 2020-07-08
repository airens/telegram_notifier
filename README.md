# Telegram Notifier
This package provides simple notifications from your app to your Telegram chat
## Preparation:
- Create bot with BotFather and copy the `token`
- Send any message to the bot (needed to automatically get `chat_id`)
## Usage:
```python
from telegram_notifier import TelegramNotifier
token = os.environ.get("TELEGRAM_BOT_TOKEN")
notifier = TelegramNotifier(token)
notifier.send("Test message")
```
