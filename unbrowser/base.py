import requests, json


class Response(object):
    def __init__(self, base_url, response):
        self.response = response
        self.base_url = base_url
        self.json = self.response.json

    def download_url(self, filename=None):
        url_parts = [self.base_url, self.json['download_path']]
        if filename is not None:
            url_parts.append(filename)
        return ''.join(url_parts)


class Unbrowser(object):
    def __init__(self, unbrowser_url, endpoint_path, user, access_key):
        self.unbrowser_url = unbrowser_url.strip('/')
        self.endpoint_path = endpoint_path
        self.url = '/'.join([self.unbrowser_url, self.endpoint_path])
        self.user = user
        self.access_key = access_key

    def _request(self, method_func, data_dict):
        print json
        return Response(
            self.unbrowser_url,
            method_func(self.url, data=data_dict, auth=(self.user, self.access_key, ))
        )

    def post(self, js):
        """ Post the js passed, and return the response. """
        request = {
            'js_script': js
        }

        return self._request(requests.post, request)
