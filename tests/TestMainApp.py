import unittest
from src.main import make_api_call, app
from fastapi.testclient import TestClient
from enum import Enum

class Messages(Enum):
    NO_URL = "Didn't receive URL"
    INVALID_NUMBER_OF_IMAGES = "Number of received URLs should be 20"
    ROOT_MESSAGE = "Hello, it is my app using FastAPI and Docker"
    REQUEST_NOT_SUCCEEDED = ""


class TestMainApp(unittest.TestCase):

    def test_make_api_call(self):
        make_api_call()

    def test_root(self):
        client = TestClient(app)
        response = client.get("/")
        message = "Hello, it is my app using FastAPI and Docker"
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.text), type(message))

if __name__ == "__main__":
    unittest.main()
