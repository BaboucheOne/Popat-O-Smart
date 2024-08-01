from pymongo import MongoClient
from pymongo.collection import Collection

from src.application.device.device_browser import DeviceBrowser
from src.application.device.device_service import DeviceService
from src.domain.report.report_repository import ReportRepository
from src.application.plant.plant_service import ReportService
from src.config.constant import ConfigurationFilename
from src.config.context.application_context import ApplicationContext
from src.infra.mongodb_report_repository import MongodbReportRepository


class DevelopmentContext(ApplicationContext):
    def __init__(self):
        super().__init__()
        self._load_configuration_from_file(ConfigurationFilename.DEVELOPMENT)

    def _instantiate_mongo_client(self) -> MongoClient:
        return MongoClient(
            self._configuration.mongodb_connection_string,
            connectTimeoutMS=self._configuration.mongodb_connection_timeout_ms,
            timeoutMS=self._configuration.mongodb_connection_timeout_ms,
        )

    def _instantiate_report_repository(
        self, report_collection: Collection
    ) -> ReportRepository:
        return MongodbReportRepository(report_collection)

    def _instantiate_report_service(
        self, report_repository: ReportRepository
    ) -> ReportService:
        return ReportService(report_repository)

    def _instantiate_device_service(self) -> DeviceService:
        device_browser = DeviceBrowser()
        return DeviceService(device_browser)
