import time
import requests


class request:
    @staticmethod
    def _request(url, method, json=None):
        while True:
            r = requests.request(method, url, json=json)
            if r.status_code != 429:
                return r
            else:
                time.sleep(0.5)

    @staticmethod
    def get(url, json=None):
        return request._request(url, 'GET', json=json)

    @staticmethod
    def post(url, json=None):
        return request._request(url, 'POST', json=json)

    @staticmethod
    def put(url, json):
        return request._request(url, 'PUT', json=json)

    @staticmethod
    def delete(url):
        return request._request(url, 'DELETE')
