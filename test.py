from psyduck import Duckdns, DuckdnsErrorException
import unittest
from mock import patch

class MockResponse():
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

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

    @patch('psyduck.requests')
    def test_update_is_called(self, mock_requests):
        duckdns = Duckdns('domain', 'token', 'myip')
        try:
            duckdns.update()
        except DuckdnsErrorException:
            pass
        mock_requests.get.assert_called_with(duckdns._get_url())

    @patch('psyduck.requests')
    def test_update_is_ok(self, mock_requests):
        duckdns = Duckdns('domain', 'token', 'myip')
        mock_requests.get.return_value = MockResponse(200, 'OK')
        duckdns.update()

    @patch('psyduck.requests')
    def test_update_is_not_ok(self, mock_requests):
        duckdns = Duckdns('domain', 'token', 'myip')
        mock_requests.get.return_value = MockResponse(200, 'KO')
        self.assertRaises(DuckdnsErrorException, duckdns.update)