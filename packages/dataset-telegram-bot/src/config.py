import os

from dotenv import load_dotenv
from spamirai_dataset_common import DataLabel


class Config:
    def __init__(self):
        load_dotenv()

        self._telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self._super_admin_id = int(os.getenv("SUPER_ADMIN_ID"))
        self._dataset_layer_name = os.getenv("DATASET_LAYER_NAME")
        self._default_label = DataLabel(os.getenv("DEFAULT_LABEL"))
        self._default_source = os.getenv("DEFAULT_SOURCE")

    @property
    def telegram_bot_token(self) -> str:
        return self._telegram_bot_token

    @property
    def super_admin_id(self) -> int:
        return self._super_admin_id

    @property
    def dataset_layer_name(self) -> str:
        return self._dataset_layer_name

    @property
    def default_label(self) -> DataLabel:
        return self._default_label

    @property
    def default_source(self) -> str:
        return self._default_source


config = Config()
