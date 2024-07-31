from dataclasses import dataclass
from uuid import UUID


@dataclass
class PlantReport:
    plant_id: UUID
    report_id: UUID
    timestamp: int
    humidity: float

    def __str__(self):
        return f"{self.plant_id} {self.report_id} {self.timestamp} {self.humidity}"
