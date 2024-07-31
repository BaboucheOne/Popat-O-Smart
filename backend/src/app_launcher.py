import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.plant.plant_resource import router as plant_resource
from src.api.device.device_resource import router as device_resource
from src.api.health_resource import router as health_resource

from src.application.device.device_browser import DeviceBrowser
from src.application.device.device_service import DeviceService
from src.application.plant.plant_service import PlantService
from src.config.service_locator import ServiceLocator


def launch():
    app = setup_app()

    device_browser = DeviceBrowser()

    ServiceLocator.register_dependency(PlantService, PlantService())
    ServiceLocator.register_dependency(PlantService, DeviceService(device_browser))

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
    app.include_router(device_resource)
