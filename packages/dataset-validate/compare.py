import os

from dotenv import load_dotenv
from src import reports_comparator


def main():
    load_dotenv()

    models_to_compare = os.getenv("MODELS_TO_COMPARE").split(",")

    if len(models_to_compare) % 2 != 0:
        raise Exception("models to compare length must be even")

    for index in range(0, len(models_to_compare), 2):
        reports_comparator.compare(
            models_to_compare[index],
            models_to_compare[index + 1],
        )


if __name__ == "__main__":
    main()
