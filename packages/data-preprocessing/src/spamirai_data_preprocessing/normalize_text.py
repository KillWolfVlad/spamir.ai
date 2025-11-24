import re

import emoji


def _to_lower(text: str) -> str:
    return text.lower()


def _replace_emoji(text: str) -> str:
    return emoji.replace_emoji(text, replace="[EMOJI]")


def _replace_whitespaces(text: str) -> str:
    # https://symbl.cc/ru/00A0/
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-2000
    return re.sub(r"[^\S\n]|[\u00a0\u2000-\u200A]", " ", text)


def _remove_extra_unicode_chars(text: str) -> str:
    # https://symbl.cc/ru/00AD/
    # https://symbl.cc/ru/0605/
    # https://symbl.cc/ru/061C/
    # https://symbl.cc/ru/06DD/
    # https://symbl.cc/ru/180E/
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-200B
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-202A
    # https://symbl.cc/ru/2060/
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-2061
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-2066
    # https://symbl.cc/ru/unicode/blocks/general-punctuation/#subblock-206A
    # https://symbl.cc/ru/FEFF/
    # https://symbl.cc/ru/unicode/blocks/tags/
    return re.sub(
        r"[\u00ad\u0605\u061C\u06DD\u180e\u200B-\u200F\u202a-\u202e\u2060\u2061-\u2064\u2066-\u2069\u206A-\u206F\ufeff\U000e0000-\U000e007f]",
        "",
        text,
    )


def _replace_urls(text: str) -> str:
    return re.sub(r"https?://\S+", "[URL]", text)


def _replace_mentions(text: str) -> str:
    return re.sub(r"@[a-z0-9_]{5,32}", "[MENTION]", text)


def _replace_phones(text: str) -> str:
    return re.sub(r"\+\d{11}", "[PHONE]", text)


def _trim(text: str) -> str:
    return text.strip()


def _remove_extra_spaces(text: str) -> str:
    return re.sub(r"[^\S\n]{2,}", " ", text)


_normalize_text_middlewares = [
    _to_lower,
    _replace_emoji,
    _replace_whitespaces,
    _remove_extra_unicode_chars,
    _replace_urls,
    _replace_mentions,
    _replace_phones,
    _trim,
    _remove_extra_spaces,
]


def normalize_text(text: str) -> str:
    result = text

    for middleware in _normalize_text_middlewares:
        result = middleware(result)

    return result
