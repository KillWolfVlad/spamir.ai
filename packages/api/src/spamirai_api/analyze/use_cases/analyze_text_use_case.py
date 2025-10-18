from spamirai_data_preprocessing import normalize_text
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

from ...config import config
from ..dtos import AnalyzeResponseDto, AnalyzeTextRequestDto
from ..enums import AnalyzeResponseLabel

tokenizer = AutoTokenizer.from_pretrained(config.text_model_path)
model = AutoModelForSequenceClassification.from_pretrained(config.text_model_path)

pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)


def analyze_text_use_case(req: AnalyzeTextRequestDto) -> AnalyzeResponseDto:
    normalized_text = normalize_text(req.text)

    predict = pipe(normalized_text)[0]

    is_spam = (
        predict["label"] == "spam" and predict["score"] >= config.text_score_threshold
    )

    return AnalyzeResponseDto(
        is_spam=is_spam,
        label=AnalyzeResponseLabel(predict["label"]),
        score=predict["score"],
    )
