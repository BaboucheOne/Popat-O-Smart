import uuid
from uuid import UUID

from src.domain.plant.plant_report import PlantReport


class PlantReportFactory:
    def __init__(self):
        pass

    def create(self, plant_id: UUID, timestamp: int, humidity: float) -> PlantReport:
        return PlantReport(plant_id, uuid.uuid4(), timestamp, humidity)
