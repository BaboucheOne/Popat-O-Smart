class UnableToGetDeviceInfoException(RuntimeError):

    MESSAGE: str = "Unable to get device info from %s."

    def __init__(self, device_name: str):
        super().__init__(self.MESSAGE % device_name)
