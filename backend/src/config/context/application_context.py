import abc
from typing import Tuple, List

from pymongo import MongoClient
from pymongo.collection import Collection

from src.application.device.device_service import DeviceService
from src.domain.report.report_repository import ReportRepository
from src.application.plant.plant_service import ReportService
from src.config.dotenv_configuration import DotEnvConfiguration
from src.domain.fastapi_client import FastApiClient
from src.config.service_locator import ServiceLocator


class ApplicationContext(abc.ABC):
    def __init__(self):
        self._configuration: DotEnvConfiguration = DotEnvConfiguration()

    def _load_configuration_from_file(self, filename: str):
        self._configuration.from_file(filename)

    def start_application(self):
        FastApiClient().run(
            self._configuration.server_ip, self._configuration.server_port
        )

    def build_application(self):
        ServiceLocator.clear()

        mongo_client = self._instantiate_mongo_client()
        report_collection = self.__instantiate_report_collection(mongo_client)
        report_repository = self._instantiate_report_repository(report_collection)

        report_service = self._instantiate_report_service(report_repository)
        device_service = self._instantiate_device_service()

        self.__register_dependencies(
            [
                (ReportService, report_service),
                (DeviceService, device_service),
            ]
        )

    def __register_dependencies(self, dependencies: List[Tuple[type, any]]):
        for dependency_type, dependency_instance in dependencies:
            ServiceLocator.register_dependency(dependency_type, dependency_instance)

    def __instantiate_report_collection(self, client: MongoClient) -> Collection:
        database = client[self._configuration.mongodb_database_name]
        return database[self._configuration.report_collection_name]

    @abc.abstractmethod
    def _instantiate_mongo_client(self) -> MongoClient:
        pass

    @abc.abstractmethod
    def _instantiate_report_repository(
        self, report_collection: Collection
    ) -> ReportRepository:
        pass

    @abc.abstractmethod
    def _instantiate_report_service(
        self, report_repository: ReportRepository
    ) -> ReportService:
        pass

    @abc.abstractmethod
    def _instantiate_device_service(self) -> DeviceService:
        pass
