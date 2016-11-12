import unittest
import json
from api import app


class ApiTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # def test_home_status_code(self):
    #     result = self.app.get('/')
    #     self.assertEqual(result.status_code, 200)

    def test_api_returnsValidJson(self):
        result = self.app.get("/prices/e17")

        # No exception thrown means test has passed
        json.dumps(str(result.data))

    def test_api_withLowerOutcode_returnsCorrectData(self):
        outcode = "e17"
        result = self.app.get("/prices/" + outcode)

        self.assertTrue(outcode.upper() in str(result.data))

    def test_api_withUpperOutcode_returnsCorrectData(self):
        outcode = "E17"
        result = self.app.get("/prices/" + outcode)

        self.assertTrue(outcode in str(result.data))

    def test_api_withInvalidOutcode_returnsError(self):
        result = self.app.get("/prices/void")

        self.assertEqual(result.status_code, 500)
        self.assertTrue("error" in str(result.data))


if __name__ == '__main__':
    unittest.main()
