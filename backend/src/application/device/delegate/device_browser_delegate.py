import abc

from src.domain.device.device import Device


class DeviceBrowserDelegate(abc.ABC):
    @abc.abstractmethod
    def add_device(self, device: Device):
        pass

    @abc.abstractmethod
    def remove_device(self, device: Device):
        pass
