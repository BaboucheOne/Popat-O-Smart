from fastapi import APIRouter, Depends

from src.api.device.response.get_devices_response import GetDevicesResponse
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
    return GetDevicesResponse(devices)
