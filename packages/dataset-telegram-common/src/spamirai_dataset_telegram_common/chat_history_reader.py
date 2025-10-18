import json
from typing import Any, Generator


def _get_message_text(text: Any) -> str:
    if isinstance(text, str):
        return text

    if isinstance(text, list):
        return "".join([x["text"] if isinstance(x, dict) else x for x in text])

    raise TypeError(f"unsupported type: {type(text)}")


class ChatHistoryReader:
    def __init__(self, chat_history_path: str):
        self._chat_history_path = chat_history_path

    def read_all(self) -> Generator[str, None, None]:
        messages = []

        with open(self._chat_history_path, "r") as f:
            messages = json.load(f)["messages"]

        for message in messages:
            if message["type"] != "message":
                continue

            yield _get_message_text(message["text"])
