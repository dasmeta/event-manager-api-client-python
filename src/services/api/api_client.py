import http
import jwt
import os
import json

class ApiClient:

    __api_host = None
    __base_path = None
    __jwt_token = None
    __logger = None

    def __init__(self, api_host, base_path, use_jwt=True, logger=None):
        self.__api_host = api_host
        self.__base_path = base_path
        self.__logger = logger

        if use_jwt:
            self.__jwt_token = jwt.encode(
                {
                    "id": os.getenv('API_USER_ID'),
                    "guid": os.getenv('API_USER_GUID'),
                    "role": {
                        "name": os.getenv('API_USER_ROLE_NAME'),
                        "type": os.getenv('API_USER_ROLE_TYPE'),
                    }
                },
                os.getenv('JWT_SECRET'),
                algorithm=os.getenv('JWT_ALGORITHM')
            )

    def call_endpoint(self, path, method="GET", body="", headers={"Content-type": "application/json"}):
        conn = http.client.HTTPConnection(self.__api_host)

        if self.__jwt_token is not None:
            headers["Authorization"] = "Bearer {}".format(self.__jwt_token)

        r = {
            'self.__api_host': self.__api_host,
            'method': method,
            'path': self.__base_path + path,
            'body': body,
            'headers': headers,
        }
        self.__logger.info('rrrrrrrrr')
        self.__logger.info(r)

        conn.request(method, self.__base_path + path, body, headers)
        response = conn.getresponse()

        try:
            body = json.loads(response.read())
        except:
            body = {}

        conn.close()

        if not (response.status == http.HTTPStatus.OK or response.status == http.HTTPStatus.CREATED
                or response.status == http.HTTPStatus.NO_CONTENT):
            raise Exception("Request Failed | body:" + str(body))

        return body
