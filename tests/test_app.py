import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_main_route(self):
        # Test the main route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "I am enhancing the API")

    def test_healthcheck_route(self):
        # Test the healthcheck route
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "OK")

    def test_new_route(self):
        # Test the new route
        response = self.app.get('/new')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "I am enhancing the API")

if __name__ == '__main__':
    unittest.main() 