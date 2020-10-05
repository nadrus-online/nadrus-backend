import logging
import os
from logging.config import fileConfig


class BaseConfig:
    """Base configurations - shared between all sub configurations"""
    def __init__(self):
        # Logging
        self.LOGGING_CONFIGURATION_FILE = 'config/logging_config.ini'

    def get_logger(self):
        """:return: The application logger"""
        fileConfig(os.path.abspath(self.LOGGING_CONFIGURATION_FILE))
        return logging.getLogger()


class ProdConfig(BaseConfig):
    """Production specific configurations"""
    NAME = 'prod'

    def __init__(self):
        super().__init__()
        self.MENTORS_SHEET_ID = os.environ.get('MENTORS_SHEET_ID')
        self.SHEET_API_KEY = os.environ.get('SHEET_API_KEY')


class DevConfig(BaseConfig):
    """Dev specific configurations"""
    NAME = 'dev'

    def __init__(self):
        super().__init__()
        self.MENTORS_SHEET_ID = '1TU7aP-uo630cE7vRlhPCRsov3pMUwxODp2eCuTGhsHo'
        self.SHEET_API_KEY = '<key>'


class ConfigLoader:
    """Configurations loader"""
    @staticmethod
    def get_config(env):
        """:return: The configurations for the given env"""
        env = 'dev' if env == 'dev' else 'production'
        BaseConfig().get_logger().info('Loading %s configurations', env)
        return DevConfig() if env == DevConfig.NAME else ProdConfig()
