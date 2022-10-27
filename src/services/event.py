from services.api.events_api_client import EventsApiClient


class EventService:
    __api_client = None

    def __init__(self, logger):
        self.__api_client = EventsApiClient(logger)

    def publish(self, topic, data, dataSource, traceId, entityProps = {}):
        return self.__api_client.publish(topic, data, dataSource, traceId, entityProps)
