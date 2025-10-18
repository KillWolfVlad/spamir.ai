import uuid
from typing import Optional

from .data_label import DataLabel


class DataItem:
    def __init__(
        self,
        text: str,
        label: DataLabel,
        source: str,
        id_: Optional[uuid.UUID] = None,
    ):
        self._text = text
        self._label = label
        self._source = source
        self._id = id_ or uuid.uuid4()

    @property
    def text(self) -> str:
        return self._text

    @property
    def label(self) -> DataLabel:
        return self._label

    @property
    def source(self) -> str:
        return self._source

    @property
    def id(self) -> uuid.UUID:
        return self._id
