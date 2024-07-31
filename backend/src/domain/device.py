class Device:
    def __init__(self, name: str, ip_address: str, port: int):
        self.name = name
        self.ip_address = ip_address
        self.port = port

    def __eq__(self, other):
        if not isinstance(other, Device):
            return False

        return self.ip_address == other.ip_address and self.port == other.port

    def __hash__(self):
        return hash((self.ip_address, self.port))
