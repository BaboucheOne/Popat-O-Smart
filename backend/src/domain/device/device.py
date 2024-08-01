from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class Device(JsonSchemaMixin):
    name: str
    ip_address: str
    port: int

    def __eq__(self, other):
        if not isinstance(other, Device):
            return False

        return self.ip_address == other.ip_address and self.port == other.port

    def __hash__(self):
        return hash((self.ip_address, self.port))
