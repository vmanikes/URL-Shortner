import unittest
from URL_shortner import checkConnection,uuid_gen
import redis

class Testing(unittest.TestCase):

    def test_connection(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        code = checkConnection(r)
        self.assertEqual(code,200)

    def test_connection1(self):
        r = redis.StrictRedis(host='', port=6379, db=0)
        code = checkConnection(r)
        self.assertEqual(code,400)

    def test_connection2(self):
        r = redis.StrictRedis(host='localhost', port=None, db=0)
        code = checkConnection(r)
        self.assertEqual(code,400)

    def test_url_none(self):
        uuid = uuid_gen(None)
        self.assertEqual(uuid,401)
