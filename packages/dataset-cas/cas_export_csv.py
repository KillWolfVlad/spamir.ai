from typing import Generator

import requests
from src import BaseCasImporter


class Importer(BaseCasImporter):
    def load_user_ids(self) -> Generator[str, None, None]:
        r = requests.get("https://api.cas.chat/export.csv")
        r.raise_for_status()

        for user_id in r.text.splitlines():
            yield user_id


def main():
    Importer().run()


if __name__ == "__main__":
    main()
