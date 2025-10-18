from pathlib import Path

import pandas as pd
from pandas import DataFrame
from spamirai_data_preprocessing import normalize_text
from spamirai_dataset_common import dataset_paths


class DatasetLayersLoader:
    def __init__(self):
        df_patch = (
            pd.concat(
                [
                    pd.read_csv(x)
                    for x in dataset_paths.get_all_dataset_layer_patch_paths()
                ]
            )
            .drop_duplicates(
                subset=["id"],
                keep="last",
            )
            .reset_index(drop=True)
        )

        self._patch = dict()
        self._text_to_exclude = set()

        for index, row in df_patch.iterrows():
            self._patch[row["id"]] = row["action"]

    def load_all(self):
        return pd.concat(
            [self._load_layer(x) for x in dataset_paths.get_all_dataset_layer_paths()]
        ).reset_index(drop=True)

    def _load_layer(self, layer_path: Path) -> DataFrame:
        df = pd.read_csv(layer_path)

        df = df[df.apply(lambda x: self._filter_item(x), axis=1)]
        df = df.apply(lambda x: self._normalize_item(x), axis=1)

        return df.reset_index(drop=True)

    def _filter_item(self, item: dict) -> bool:
        if item["text"] in self._text_to_exclude:
            return False

        if item["id"] in self._patch:
            match self._patch[item["id"]]:
                case "exclude":
                    self._text_to_exclude.add(item["text"])
                    return False

        return True

    def _normalize_item(self, item: dict) -> dict:
        item["text"] = normalize_text(item["text"])

        return item
