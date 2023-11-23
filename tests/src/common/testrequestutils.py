import unittest

from src.common.requestutils import make_query_or, make_query_and, send_resquest


class TestRequestUtils(unittest.TestCase):
    def test_make_query_or(self):
        KEYWORDS = [
            "Taylor Swift | The Eras Tour",
            "The Exorcist: Believer",
        ]
        query = make_query_or(KEYWORDS)
        self.assertEqual(
            query, '"Taylor Swift | The Eras Tour" OR "The Exorcist: Believer"'
        )

    def test_make_query_and(self):
        KEYWORDS = [
            "Taylor Swift | The Eras Tour",
            "The Exorcist: Believer",
        ]
        query = make_query_and(KEYWORDS)
        self.assertEqual(
            query, '"Taylor Swift | The Eras Tour" AND "The Exorcist: Believer"'
        )

    def test_send_request(self):
        url = "https://www.google.com"
        response = send_resquest(url)
        self.assertTrue(response is not None and response.status_code == 200, True)


if __name__ == "__main__":
    unittest.main()
