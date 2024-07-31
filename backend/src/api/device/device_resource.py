from fastapi import APIRouter, Depends
from fastapi.responses import Response
from starlette import status

from src.application.device.device_service import DeviceService
from src.config.service_locator import ServiceLocator

router = APIRouter()


@router.get("/devices")
async def get_devices(
    device_service: DeviceService = Depends(
        lambda: ServiceLocator.get_dependency(DeviceService)
    ),
):

    devices = device_service.get_devices()
    return Response(status_code=status.HTTP_200_OK)
