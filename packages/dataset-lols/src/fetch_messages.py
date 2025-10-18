import calendar
import locale
from datetime import date
from typing import Generator

from bs4 import BeautifulSoup
from requests_sse import EventSource


def fetch_messages(current_date: date) -> Generator[dict, None, None]:
    locale.setlocale(locale.LC_ALL, "en_US")

    request_url = f"https://lols.bot/{current_date.year}/{calendar.month_name[current_date.month]}-{current_date.day}/?sse"

    with EventSource(request_url, timeout=60) as event_source:
        for event in event_source:
            if event.data == "EOF":
                event_source.close()

                break
            else:
                bs = BeautifulSoup(event.data, "html.parser").contents[0]

                if bs.attrs.get("id") is not None:
                    content = bs.find("div", class_="message__text__content")

                    if content:
                        time_div = content.find("div", class_="message__time")

                        if time_div:
                            time_div.decompose()

                        a = content.find("a")

                        if a:
                            a.decompose()

                        text = content.get_text(separator="\n", strip=True)

                        yield {"text": text}
