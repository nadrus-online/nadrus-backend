import httplib2
from apiclient import discovery

from app import app

config = app.config['config']
logger = config.get_logger()

service = None


class GoogleApi:
    @staticmethod
    def get_service():
        global service
        if service:
            logger.info('getting existing Google Sheets service')
            return service
        logger.info('creating a new Google Sheets service')
        service = discovery.build(
            'sheets',
            'v4',
            http=httplib2.Http(),
            discoveryServiceUrl='https://sheets.googleapis.com/$discovery/rest?version=v4',
            developerKey=config.SHEET_API_KEY,
            cache_discovery=False)
        return service
