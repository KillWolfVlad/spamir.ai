import os
from pathlib import Path

from natsort import natsorted

from .fs_utils import mkdirp


class DatasetPaths:
    def __init__(self):
        self._dataset_extension = ".csv"
        self._patch_suffix = "_patch"

        self._dataset_dir = (
            Path(__file__).parent.parent.parent.parent.parent / "dataset"
        )

        mkdirp(self.dataset_dir)
        mkdirp(self.dataset_layers_dir)

    @property
    def dataset_dir(self) -> Path:
        return self._dataset_dir

    @property
    def dataset_layers_dir(self) -> Path:
        return self.dataset_dir / "layers"

    @property
    def train_dataset_path(self) -> Path:
        return self.dataset_dir / f"train{self._dataset_extension}"

    @property
    def test_dataset_path(self) -> Path:
        return self.dataset_dir / f"test{self._dataset_extension}"

    @property
    def validation_dataset_path(self) -> Path:
        return self.dataset_dir / f"validation{self._dataset_extension}"

    @property
    def tuning_dataset_path(self) -> Path:
        return self.dataset_dir / f"tuning{self._dataset_extension}"

    def get_dataset_layer_path(self, layer_name: str) -> Path:
        return self.dataset_layers_dir / f"{layer_name}{self._dataset_extension}"

    def get_all_dataset_layer_paths(self) -> list[Path]:
        return self._get_all_dataset_layer_paths(False)

    def get_all_dataset_layer_patch_paths(self) -> list[Path]:
        return self._get_all_dataset_layer_paths(True)

    def _get_all_dataset_layer_paths(self, allow_patches: bool) -> list[Path]:
        files = [
            self.dataset_layers_dir / x
            for x in os.listdir(self.dataset_layers_dir)
            if Path(x).suffix == self._dataset_extension
            and not x.startswith("_")
            and Path(x).stem.endswith(self._patch_suffix) == allow_patches
        ]

        return natsorted(files)


dataset_paths = DatasetPaths()
