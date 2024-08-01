from typing import List
from uuid import UUID

from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.results import InsertOneResult

from src.domain.report.report_repository import ReportRepository
from src.domain.report.report import Report
from src.infra.assembler.report_assembler import ReportAssembler
from src.infra.exception.cannot_add_report_exception import CannotAddReportException
from src.infra.exception.reports_not_found_exception import ReportsNotFoundException

from src.infra.constant import ReportJsonKey


class MongodbReportRepository(ReportRepository):
    def __init__(self, report_collection: Collection):
        self.__report_collection = report_collection
        self.__report_assembler = ReportAssembler()

    def add_report(self, report: Report):
        result: InsertOneResult = self.__report_collection.insert_one(
            self.__report_assembler.to_dict(report)
        )

        if result.inserted_id is None:
            raise CannotAddReportException(report)

    def get_reports(self, plant_id: UUID) -> List[Report]:
        reports_response: Cursor = self.__report_collection.find(
            {ReportJsonKey.PLANT_ID: str(plant_id)}
        )

        if not reports_response.alive:
            raise ReportsNotFoundException(plant_id)

        return [
            self.__report_assembler.from_json(report) for report in reports_response
        ]
