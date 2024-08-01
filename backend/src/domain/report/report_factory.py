import uuid
from uuid import UUID

from src.domain.report.report import Report


class ReportFactory:
    def __init__(self):
        pass

    def create(self, plant_id: UUID, timestamp: int, humidity: float) -> Report:
        return Report(plant_id, uuid.uuid4(), timestamp, humidity)
