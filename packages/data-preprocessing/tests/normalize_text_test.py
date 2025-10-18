import unicodedata

import pandas as pd
import pytest
from spamirai_data_preprocessing import normalize_text
from spamirai_dataset_common import dataset_paths

test_cases = [
    (
        "lover text",
        "ПриВет!",
        "привет!",
    ),
    (
        "replace emoji",
        "❗️❗️❗️Друзья, изменилось место проведения дизайн-завтрака в Петербурге.",
        "[EMOJI][EMOJI][EMOJI]друзья, изменилось место проведения дизайн-завтрака в петербурге.",
    ),
    (
        "replace one url",
        "拒绝再做接盘侠！https://t.me/+KHWL-U8EMso5YmZk",
        "拒绝再做接盘侠！[URL]",
    ),
    (
        "replace two urls",
        "смешные видео\nhttps://youtu.be/3WSG0T_GYfI?si=s2MhXCMXPI879rcN\nhttps://youtu.be/guZIRDQ3qls?si=vPUZZihkULtAXl-H",
        "смешные видео\n[URL]\n[URL]",
    ),
    (
        "replace one mention",
        "ПИШи В ЛС @Manager_Alex1488",
        "пиши в лс [MENTION]",
    ),
    (
        "replace two mentions",
        "ПИШи В ЛС @Manager_Alex1488 или @sabste",
        "пиши в лс [MENTION] или [MENTION]",
    ),
    (
        "handle mention in url",
        "https://t.me/@qwerty 👉@gorsga",
        "[URL] [EMOJI][MENTION]",
    ),
    (
        "trim",
        "     🔥 Результат виден сразу после старта!    ",
        "[EMOJI] результат виден сразу после старта!",
    ),
    (
        "remove extra spaces",
        "     🔥     Результат        виден       сразу     после        старта!       ",
        "[EMOJI] результат виден сразу после старта!",
    ),
]


@pytest.mark.parametrize(
    "text, expected_text",
    [(x[1], x[2]) for x in test_cases],
    ids=[x[0] for x in test_cases],
)
def test_normalize_text(text: str, expected_text: str):
    assert normalize_text(text) == expected_text


def test_invisible_chars():
    for layer_path in dataset_paths.get_all_dataset_layer_paths():
        df = pd.read_csv(layer_path)

        for _, item in df.iterrows():
            normalized_text = normalize_text(item["text"])

            for char in normalized_text:
                char_category = unicodedata.category(char)

                if char_category in ["Cf"]:
                    print()
                    print(hex(ord(char)))
                    print(item)

                    assert char_category not in ["Cf"]
