# spamir.ai

<p align="center">
  <img src="./brand/logo.png" width="250"/>
  <br>
</p>

AI-Powered spam detection service :zap:

## Demo

<https://huggingface.co/spaces/KillWolfVlad/spamir.ai-demo>

## Models

See [spamir.ai collection](https://huggingface.co/collections/KillWolfVlad/spamirai-68b349b23fa0be2045096b40) on Hugging Face.

## Usage

```bash
docker run -e API_KEYS=xxx,yyy -p 8000:8000 ghcr.io/killwolfvlad/spamirai-api:latest
```

You can find versions in [GitHub Packages](https://github.com/KillWolfVlad/spamir.ai/pkgs/container/spamirai-api).

> WARNING! Only CPU supported for inference. If you want GPU support you must build your own version of API.

### Service endpoints

- Swagger: <http://localhost:8000/docs>
- Readiness probe: <http://localhost:8000/health/readiness>
- Liveness probe: <http://localhost:8000/health/liveness>
- Metrics: <http://localhost:8000/metrics>

### Analyze Text endpoint

```http
POST http://localhost:8000/api/v1/analyze/text
Authorization: Bearer xxx
Content-Type: application/json

{
  "text": "Заработок от 100$ в день.\nПишите в л.с."
}
```

Example response for spam:

```json
{
  "isSpam": true,
  "label": "spam",
  "score": 0.9999480247497559
}
```

Example response for not spam:

```json
{
  "isSpam": false,
  "label": "not_spam",
  "score": 0.9999113082885742
}
```

## Maintainers

- [@KillWolfVlad](https://github.com/KillWolfVlad)

## License

This repository is released under version 2.0 of the
[Apache License](https://www.apache.org/licenses/LICENSE-2.0).
