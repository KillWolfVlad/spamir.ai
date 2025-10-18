from ...common import BaseDto
from ..enums import AnalyzeResponseLabel


class AnalyzeResponseDto(BaseDto):
    is_spam: bool
    label: AnalyzeResponseLabel
    score: float
