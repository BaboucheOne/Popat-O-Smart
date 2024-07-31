import re

from zeroconf import ServiceListener, Zeroconf

from src.application.device.delegate.device_service_delegate import (
    DeviceServiceDelegate,
)
from src.application.device.exception.unable_to_get_device_info_exception import (
    UnableToGetDeviceInfoException,
)
from src.domain.device import Device
from src.domain.device_factory import DeviceFactory


class DeviceListener(ServiceListener):

    DEVICE_NAME_REGEX: str = r"water-plant"

    def __init__(self, device_service_delegate: DeviceServiceDelegate):
        self.__device_factory = DeviceFactory()
        self.__device_service_delegate = device_service_delegate

    def __is_device_match_required_name(self, device: Device) -> bool:
        return bool(re.search(self.DEVICE_NAME_REGEX, device.name))

    def __get_device(self, zc: Zeroconf, type_: str, name: str) -> Device:
        device_info = zc.get_service_info(type_, name)
        if not device_info:
            raise UnableToGetDeviceInfoException(name)
        return self.__device_factory.create(name, device_info)

    def add_service(self, zc: Zeroconf, type_: str, name: str):
        try:
            device = self.__get_device(zc, type_, name)
            if self.__is_device_match_required_name(device):
                self.__device_service_delegate.add_device(device)
        except UnableToGetDeviceInfoException as e:
            print(e)

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        try:
            device = self.__get_device(zc, type_, name)
            if self.__is_device_match_required_name(device):
                self.__device_service_delegate.remove_device(device)
        except UnableToGetDeviceInfoException as e:
            print(e)
