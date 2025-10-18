import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        self._host = os.getenv("HOST")
        self._port = int(os.getenv("PORT"))
        self._workers_count = int(os.getenv("WORKERS_COUNT"))

        self._text_model_path = os.getenv("TEXT_MODEL_PATH")
        self._text_score_threshold = float(os.getenv("TEXT_SCORE_THRESHOLD"))

        self._api_keys = set(os.getenv("API_KEYS").split(","))

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def workers_count(self) -> int:
        return self._workers_count

    @property
    def text_model_path(self) -> str:
        return self._text_model_path

    @property
    def text_score_threshold(self) -> float:
        return self._text_score_threshold

    @property
    def api_keys(self) -> set[str]:
        return self._api_keys


config = Config()
