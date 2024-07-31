from uuid import UUID
from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class PlantReport(JsonSchemaMixin):
    plant_id: UUID
    report_id: UUID
    timestamp: int
    humidity: float

    def __str__(self):
        return f"{self.plant_id} {self.report_id} {self.timestamp} {self.humidity}"
