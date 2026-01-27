################################################################################

ARG BUILDER_IMAGE=python:3.13.7-slim-trixie
ARG RUNTIME_IMAGE=python:3.13.7-slim-trixie

################################################################################

FROM ${BUILDER_IMAGE} AS builder

WORKDIR /api

COPY --from=ghcr.io/astral-sh/uv:0.9.27 /uv /uvx /bin/
COPY ./ ./

RUN cd ./packages/api && \
    uv sync --locked --no-python-downloads --no-dev --no-editable

################################################################################

FROM ${RUNTIME_IMAGE} AS runtime

RUN groupadd --gid 1000 api && \
    useradd --uid 1000 --gid api --shell /bin/bash --create-home api

WORKDIR /api

COPY --from=builder /api/.venv ./.venv

ENV PATH="/api/.venv/bin:$PATH"

ENV HOST=0.0.0.0
ENV PORT=8000
ENV WORKERS_COUNT=1

ENV TEXT_MODEL_PATH="/api/models/text"
ENV TEXT_SCORE_THRESHOLD="0.99"

EXPOSE 8000

USER api

CMD ["spamirai-api"]
