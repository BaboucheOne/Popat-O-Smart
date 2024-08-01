import abc
from typing import List
from uuid import UUID

from src.domain.report.report import Report


class ReportRepository(abc.ABC):

    @abc.abstractmethod
    def add_report(self, plant_report: Report):
        pass

    @abc.abstractmethod
    def get_reports(self, plant_id: UUID) -> List[Report]:
        pass
