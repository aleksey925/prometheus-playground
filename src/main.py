import os

import uvicorn
from fastapi import FastAPI, APIRouter
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    REGISTRY,
    CollectorRegistry,
    generate_latest,
    Gauge,
)
from prometheus_client.multiprocess import MultiProcessCollector
from starlette.requests import Request
from starlette.responses import Response

router = APIRouter()

metric = Gauge(
    name="metric",
    labelnames=["label"],
    documentation="",
    namespace="my_app",
)


@router.get("/init")
async def init_metric_view(label: str = 'default'):
    metric.labels(label=label)
    return f"metric with label={label} initialized"


@router.get("/inc")
async def inc_metric_view(label: str = 'default'):
    metric.labels(label=label).inc(1)
    return f"metric with label={label} increased"


@router.get("/set")
async def set_metric_view(value: int, label: str = 'default'):
    metric.labels(label=label).set(value)
    return f"metric with label={label} increased"


@router.get("/metrics")
async def metrics_view(request: Request):
    if "prometheus_multiproc_dir" in os.environ:
        registry = CollectorRegistry()
        MultiProcessCollector(registry)
    else:
        registry = REGISTRY

    return Response(generate_latest(registry), headers={"Content-Type": CONTENT_TYPE_LATEST})


def create_app():
    _app = FastAPI()
    _app.include_router(router)
    return _app


app = create_app()

if __name__ == '__main__':
    server = uvicorn.Server(
        uvicorn.Config(app, host="0.0.0.0", port=8000)
    )
    server.run()
