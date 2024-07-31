import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.application.device.device_service_browser import DeviceServiceBrowser


def launch():
    app = setup_app()
    DeviceServiceBrowser()
    uvicorn.run(app, host="127.0.0.1", port=8000)


def setup_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_routers(app)

    return app


def include_routers(app: FastAPI):
    # app.include_router(health_router)
    pass
