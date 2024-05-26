import requests
import unittest

class TestWebsiteReachable(unittest.TestCase):
    def test_website_reachable(self):
        url = "http://127.0.0.1:5001/weather"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
