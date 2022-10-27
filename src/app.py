from flask import Flask, request
from src.services.event import EventService
import sys
import http

app = Flask(__name__)

event_service = EventService(app.logger)

@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    try:
        event_service.publish(
            topic = data['topic'],
            data = data['data'],
            dataSource = data['dataSource'],
            traceId = data['traceId'],
            entityProps = data['entityProps']
        )
    except Exception as e:
        app.logger.exception(sys.exc_info()[0].__doc__)
        app.logger.exception(str(e))
        return {'error': 'Error at publishing.'}, http.HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}

    return {'isSuccess': 'true'}, http.HTTPStatus.CREATED, {'Content-Type': 'application/json'}
