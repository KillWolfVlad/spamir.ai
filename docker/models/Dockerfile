################################################################################

ARG BASE_IMAGE=spamirai-api:base

################################################################################

FROM ${BASE_IMAGE} AS builder

ARG TEXT_MODEL=KillWolfVlad/spamir.ai-model-tabula-rasa

USER root

RUN hf download --local-dir ./models/text ${TEXT_MODEL} \
      config.json model.safetensors special_tokens_map.json tokenizer.json tokenizer_config.json

RUN rm -rf ./models/text/.cache

################################################################################

FROM ${BASE_IMAGE} AS runtime

COPY --from=builder /api/models ./models
