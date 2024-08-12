import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.health_resource import router as health_resource
from src.api.report.report_resource import router as report_resource
from src.api.device.device_resource import router as device_resource


class FastApiClient:
    def __init__(self):
        self.__app = FastAPI()
        self.__add_middleware()
        self.__include_routers()

    def run(self, ip_address: str, port: int):
        uvicorn.run(self.__app, host=ip_address, port=port)

    def __add_middleware(self):
        self.__app.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __include_routers(self):
        self.__app.include_router(health_resource)
        self.__app.include_router(report_resource)
        self.__app.include_router(device_resource)
