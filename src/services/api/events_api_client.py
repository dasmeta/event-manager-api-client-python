import os
import json
from .api_client import ApiClient


class EventsApiClient:
    _api_client = None
    __logger = None

    def __init__(self, logger):
        self.__logger = logger

        # Todo - enable JWT once it's suported on API side
        self._api_client = ApiClient(os.getenv('API_HOST'), '/events', False, logger)

    def publish(self, topic, data, dataSource, traceId, entityProps = {}):
        event = {
            'topic': topic,
            'data': data,
            'dataSource': dataSource,
            'traceId': traceId,
            'entityProps': entityProps
        }
        body = json.dumps(event)

        return self.__call_endpoint('', 'POST', body)

    def __call_endpoint(self, path='', method='GET', body='', headers={'Content-type': 'application/json'}):
        return self._api_client.call_endpoint(path, method, body, headers)
