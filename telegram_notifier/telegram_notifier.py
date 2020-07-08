import requests


class TelegramNotifier:
    def __init__(self, token: str, parse_mode: str = None):
        self._token = token
        self._parse_mode = parse_mode
        self._chat_id = None
        response = requests.get(f"https://api.telegram.org/bot{self._token}/getUpdates", timeout=10)
        if response.status_code == 200:
            self._chat_id = response.json()['result'][-1]['message']['chat']['id']
        assert self._chat_id is not None, "Couldn't get chat_id!"

    def send(self, msg:str):
        data = {
            "chat_id": self._chat_id,
            "text": msg
        }
        if self._parse_mode:
            data["parse_mode"] = self._parse_mode
        try:
            response = requests.get(f"https://api.telegram.org/bot{self._token}/sendMessage", data=data, timeout=10)
            if response.status_code != 200 or response.json()["ok"] is not True:
                print(f"Failed to send notification:\n\tstatus_code={response.status_code}\n\tjson:\n\t{response.json()}")
        except Exception as e:
            print(f"Failed to send notification:\n\texception:\n\t{e}")


def main():
    import os
    token = os.environ.get("TELEGRAM_TOKEN")
    notifier = TelegramNotifier(token, parse_mode="HTML")
    notifier.send("<b>Test bold text</b> and normal text")


if __name__ == '__main__':
    main()
