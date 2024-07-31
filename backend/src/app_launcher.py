import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.plant.plant_resource import router as plant_resource
from src.api.health_resource import router as health_resource
from src.application.device.device_service_browser import DeviceServiceBrowser
from src.application.plant.plant_service import PlantService
from src.config.service_locator import ServiceLocator


def launch():
    app = setup_app()
    DeviceServiceBrowser()

    ServiceLocator.register_dependency(PlantService, PlantService())

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
    app.include_router(health_resource)
    app.include_router(plant_resource)
