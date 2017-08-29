import unittest
import requests
import URL_shortner

class Testing(unittest.TestCase):

    def test_index(self):
        index = requests.get(URL_shortner.index())
        self.assertEqual(index.status_code,200)