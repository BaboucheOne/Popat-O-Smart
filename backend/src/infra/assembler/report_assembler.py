import uuid

from src.domain.report.report import Report
from src.infra.constant import ReportJsonKey


class ReportAssembler:
    def __init__(self):
        pass

    def to_dict(self, report: Report) -> dict:
        return report.to_dict()

    def from_json(self, report: dict) -> Report:
        return Report(
            uuid.UUID(report[ReportJsonKey.PLANT_ID]),
            uuid.UUID(report[ReportJsonKey.REPORT_ID]),
            report[ReportJsonKey.TIMESTAMP],
            report[ReportJsonKey.HUMIDITY],
        )
