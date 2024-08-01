from typing import List
from uuid import UUID

from src.domain.report.report_repository import ReportRepository
from src.domain.report.report import Report
from src.domain.report.report_factory import ReportFactory


class ReportService:
    def __init__(self, report_repository: ReportRepository):
        self.__report_repository = report_repository
        self.__report_factory = ReportFactory()

    def add_report(self, plant_id: UUID, timestamp: int, humidity: float):
        report = self.__report_factory.create(plant_id, timestamp, humidity)
        self.__report_repository.add_report(report)

    def get_reports(self, plant_id: UUID) -> List[Report]:
        return self.__report_repository.get_reports(plant_id)
