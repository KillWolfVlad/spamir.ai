from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_healthchecks.api.router import HealthcheckRouter, Probe
from prometheus_fastapi_instrumentator import Instrumentator

from .analyze import router as analyze_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    instrumentator.expose(app, include_in_schema=False)
    yield


app = FastAPI(
    title="spamir.ai api ⚡",
    summary="AI-Powered spam detection service - API",
    description="Demo: <https://huggingface.co/spaces/KillWolfVlad/spamir.ai-demo>\n\nMain repository: <https://github.com/KillWolfVlad/spamir.ai>",
    version="0.0.0",
    lifespan=lifespan,
)

instrumentator = Instrumentator().instrument(app)


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")


app.include_router(
    HealthcheckRouter(
        Probe(
            name="readiness",
            checks=[],
        ),
        Probe(
            name="liveness",
            checks=[],
        ),
    ),
    prefix="/health",
    include_in_schema=False,
)

app.include_router(analyze_router)
