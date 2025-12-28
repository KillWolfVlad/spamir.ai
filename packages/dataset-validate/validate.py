import os

from dotenv import load_dotenv
from src import BaseValidator
from transformers import pipeline


class Validator(BaseValidator):
    def __init__(self, model: str):
        super().__init__(model)

        self._pipe = pipeline("text-classification", model=self._model)

    def get_predict(self, text: str) -> dict:
        return self._pipe(text)[0]


def main():
    load_dotenv()

    models = os.getenv("MODELS").split(",")

    for model in models:
        Validator(model).run()


if __name__ == "__main__":
    main()
