from zeroconf import ServiceInfo

from src.domain.device.device import Device


class DeviceFactory:
    def __init__(self):
        pass

    def create(self, name: str, device_info: ServiceInfo) -> Device:
        return Device(name, device_info.parsed_scoped_addresses()[0], device_info.port)
