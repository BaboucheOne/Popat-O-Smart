import os

from dotenv import load_dotenv, find_dotenv

from src.config.constant import DotenvConfigurationKey
from src.config.exception.environment_variable_type_exception import (
    EnvironmentVariableTypeException,
)
from src.config.exception.missing_environment_variable_exception import (
    MissingEnvironmentVariableException,
)


class DotEnvConfiguration:
    def __init__(self):
        pass

    def from_file(self, filename: str):
        dotenv_path = find_dotenv(filename=filename)
        load_dotenv(dotenv_path=dotenv_path)

    def __get_variable(self, environment_variable_key: str):
        try:
            return os.getenv(environment_variable_key)
        except KeyError:
            raise MissingEnvironmentVariableException(environment_variable_key)

    def __get_string(self, environment_variable_key: str):
        try:
            return str(self.__get_variable(environment_variable_key))
        except (ValueError, TypeError):
            raise EnvironmentVariableTypeException(environment_variable_key, str)

    def __get_int(self, environment_variable_key: str):
        try:
            return int(self.__get_variable(environment_variable_key))
        except (ValueError, TypeError):
            raise EnvironmentVariableTypeException(environment_variable_key, int)

    @property
    def mongodb_connection_string(self) -> str:
        return self.__get_string(DotenvConfigurationKey.MONGODB_CONNECTION_STRING)

    @property
    def mongodb_connection_timeout_ms(self) -> int:
        return self.__get_int(DotenvConfigurationKey.MONGODB_CONNECTION_TIMEOUT_MS)

    @property
    def mongodb_database_name(self) -> str:
        return self.__get_string(DotenvConfigurationKey.MONGODB_DATABASE_NAME)

    @property
    def report_collection_name(self) -> str:
        return self.__get_string(DotenvConfigurationKey.REPORT_COLLECTION_NAME)

    @property
    def server_ip(self) -> str:
        return self.__get_string(DotenvConfigurationKey.SERVER_IP)

    @property
    def server_port(self) -> int:
        return self.__get_int(DotenvConfigurationKey.SERVER_PORT)

    @property
    def logger_filename(self) -> str:
        return self.__get_string(DotenvConfigurationKey.LOGGER_FILENAME)
