class Duckdns():

    BASEURL = 'https://www.duckdns.org/update?domains={}&token={}&ip={}'

    def __init__(self, domain, token, ip=''):
        self._domain = domain
        self._token = token
        self._ip = ip

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