from search.blocklist import block_list
from django.test import TestCase
from django.test import Client

class BlocklistTest(TestCase):

    def test_blocked_word_returns_422(self):
        client = Client()
        response = client.get("/api/?q=fuck")
        self.assertEqual(response.status_code, 422)

    def test_blocked_word_case_insensitive(self):
        client = Client()
        response = client.get("/api/?q=FUCK")
        self.assertEqual(response.status_code, 422)
