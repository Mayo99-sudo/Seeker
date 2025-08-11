import unittest
from triangulate import triangulate_ip

class TestTriangulateIP(unittest.TestCase):
    def test_invalid_ip(self):
        result = triangulate_ip("invalid_ip")
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()