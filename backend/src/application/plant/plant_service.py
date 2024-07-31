from uuid import UUID

from src.domain.plant.plant_report_factory import PlantReportFactory


class PlantService:
    def __init__(self):
        self.__plant_report_factory = PlantReportFactory()

    def add_report(self, plant_id: UUID, timestamp: int, humidity: float):
        plant_report = self.__plant_report_factory.create(plant_id, timestamp, humidity)
        print(f"report added: {plant_report}")
