import requests

class DuckdnsErrorException(Exception):
    pass

class Duckdns(object):

    BASEURL = 'https://www.duckdns.org/update?domains={}&token={}&ip={}'

    def __init__(self, domain, token, ip=''):
        self.domain = domain
        self.token = token
        self.ip = ip

    @property
    def domain(self):
        return self._domain

    @property
    def token(self):
        return self._token

    @property
    def ip(self):
        return self._ip

    @domain.setter
    def domain(self, domain):
        self._domain = domain

    @token.setter
    def token(self, token):
        self._token = token

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    def _get_url(self):
        return Duckdns.BASEURL.format(self.domain, self.token, self.ip)

    def update(self):
        r = requests.get(self._get_url())
        if r.status_code != 200 or r.text != 'OK':
            raise DuckdnsErrorException('Error updating your ip')
