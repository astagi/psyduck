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
