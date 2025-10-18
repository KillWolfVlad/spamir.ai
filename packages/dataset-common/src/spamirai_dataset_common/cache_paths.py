from pathlib import Path

from .dataset_paths import dataset_paths
from .fs_utils import mkdirp


class CachePaths:
    def __init__(self):
        mkdirp(self.cache_dir)

    @property
    def cache_dir(self) -> Path:
        return dataset_paths.dataset_dir / "cache"

    def get_cache_dir(self, name: str) -> Path:
        cache_path = self.cache_dir / name
        mkdirp(cache_path)

        return cache_path


cache_paths = CachePaths()
