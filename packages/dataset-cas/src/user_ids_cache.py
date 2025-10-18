import csv

import pandas as pd
from spamirai_dataset_common import cache_paths


class UserIdsCache:
    def __init__(self):
        self._user_ids_cache = set()
        self._user_ids_cache_path = cache_paths.get_cache_dir("cas") / "user_ids.csv"

        if self._user_ids_cache_path.exists():
            df = pd.read_csv(self._user_ids_cache_path, dtype=object)
            self._user_ids_cache = set(df["user_id"])

    def __contains__(self, user_id: str) -> bool:
        return user_id in self._user_ids_cache

    def add_all(self, user_ids: list[str]):
        user_ids_cache_exists = self._user_ids_cache_path.exists()

        with open(self._user_ids_cache_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not user_ids_cache_exists:
                writer.writerow(["user_id"])

            for user_id in user_ids:
                if user_id in self:
                    continue

                self._user_ids_cache.add(user_id)

                writer.writerow([user_id])


user_ids_cache = UserIdsCache()
