from typing import List
from zeroconf import Zeroconf, ServiceBrowser

from src.application.device.delegate.device_service_delegate import (
    DeviceServiceDelegate,
)
from src.application.device.device_listener import DeviceListener
from src.domain.device import Device


class DeviceServiceBrowser(DeviceServiceDelegate):
    def __init__(self):
        self.__zeroconf = Zeroconf()
        self.__devices: set[Device] = set()
        self.__device_listener = DeviceListener(self)
        self.__browser = ServiceBrowser(
            self.__zeroconf, "_http._tcp.local.", self.__device_listener
        )

    @property
    def devices(self) -> List[Device]:
        return list(self.__devices)

    def add_device(self, device: Device):
        if device not in self.__devices:
            self.__devices.add(device)

    def remove_device(self, device: Device):
        if device in self.__devices:
            self.__devices.remove(device)

    def stop(self):
        self.__zeroconf.close()
