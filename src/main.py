import os

import uvicorn
from fastapi import FastAPI, APIRouter
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    REGISTRY,
    CollectorRegistry,
    generate_latest, Counter,
)
from prometheus_client.multiprocess import MultiProcessCollector
from starlette.requests import Request
from starlette.responses import Response

open_page_total = Counter(
    name="open_page_total",
    labelnames=["name"],
    documentation="",
    namespace="my_app",
)


async def index_view():
    open_page_total.labels(name="index").inc(1)
    return "index page"


async def metrics_view(request: Request):
    if "prometheus_multiproc_dir" in os.environ:
        registry = CollectorRegistry()
        MultiProcessCollector(registry)
    else:
        registry = REGISTRY

    return Response(generate_latest(registry), headers={"Content-Type": CONTENT_TYPE_LATEST})


def create_app():
    app = FastAPI()
    router = APIRouter()
    router.add_api_route("/metrics", metrics_view, methods=["GET"])
    router.add_api_route("/", index_view, methods=["GET"])
    app.include_router(router)
    return app


app = create_app()

if __name__ == '__main__':
    server = uvicorn.Server(
        uvicorn.Config(app, host="0.0.0.0", port=8000)
    )
    server.run()
