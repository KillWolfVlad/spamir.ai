import os
import re
from typing import Generator

from dotenv import load_dotenv
from spamirai_dataset_telegram_common import ChatHistoryReader
from src import BaseCasImporter


class Importer(BaseCasImporter):
    def load_user_ids(self) -> Generator[str, None, None]:
        chat_history_reader = ChatHistoryReader(
            os.getenv("CAS_TELEGRAM_FEED_HISTORY_PATH"),
        )

        for message in chat_history_reader.read_all():
            user_ids = re.findall(r"#(\d+)", message)

            for user_id in user_ids:
                yield user_id


def main():
    load_dotenv()

    Importer().run()


if __name__ == "__main__":
    main()
