from src.domain.report.report import Report


class CannotAddReportException(RuntimeError):

    MESSAGE: str = "Cannot add report %s."

    def __init__(self, report: Report):
        super().__init__(self.MESSAGE % report.to_dict())
