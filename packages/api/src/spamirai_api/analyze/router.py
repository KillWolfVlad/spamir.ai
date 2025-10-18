from fastapi import APIRouter, Depends

from ..auth import verify_api_key
from .dtos import AnalyzeResponseDto, AnalyzeTextRequestDto
from .use_cases import analyze_text_use_case

router = APIRouter(
    prefix="/api/v1",
    tags=["Analyze"],
    dependencies=[Depends(verify_api_key)],
)


@router.post("/analyze/text")
def analyze_text(req: AnalyzeTextRequestDto) -> AnalyzeResponseDto:
    return analyze_text_use_case(req)
