import logging

from src import app


def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    app.run_polling()


if __name__ == "__main__":
    main()
