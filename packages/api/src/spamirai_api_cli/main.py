import uvicorn
from spamirai_api import config


def main():
    uvicorn.run(
        "spamirai_api:app",
        host=config.host,
        port=config.port,
        workers=config.workers_count,
    )


if __name__ == "__main__":
    main()
