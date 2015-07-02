import unittest
from simple_flask.rest.rest import RootREST


class SimpleRestTest(unittest.TestCase):

    def setUp(self):
        self.root = RootREST('localhost', False)
        self.app = self.root.app
        self.tester = self.app.test_client(self)

    def test_say_hallo(self):
        response = self.tester.get('/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'Hallo from CORE!')
        response = self.tester.get('/Kalimaha/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'Hallo Kalimaha from CORE!')
