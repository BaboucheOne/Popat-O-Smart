from typing import List

from src.application.device.device_browser import DeviceBrowser
from src.domain.device.device import Device


class DeviceService:
    def __init__(self, device_browser: DeviceBrowser):
        self.__device_browser = device_browser

    def get_devices(self) -> List[Device]:
        return self.__device_browser.devices
