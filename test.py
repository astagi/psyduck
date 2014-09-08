from psyduck import Duckdns
import unittest
from mock import patch

class TestPsyduck(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_dyndns_class(self):
        duckdns = Duckdns('domain', 'token')
        self.assertEqual(duckdns.domain, 'domain')
        self.assertEqual(duckdns.token, 'token')
        self.assertEqual(duckdns.ip, '')

    def test_init_dyndns_class_with_all_parameters(self):
        duckdns = Duckdns('domain', 'token', 'myip')
        self.assertEqual(duckdns.domain, 'domain')
        self.assertEqual(duckdns.token, 'token')
        self.assertEqual(duckdns.ip, 'myip')

    def test_get_url(self):
        duckdns = Duckdns('domain', 'token', 'myip')
        url = duckdns._get_url()
        base_url = 'https://www.duckdns.org/update?domains={}&token={}&ip={}'
        expected_url = base_url.format(duckdns.domain, duckdns.token,
            duckdns.ip)
        self.assertEqual(expected_url, url)