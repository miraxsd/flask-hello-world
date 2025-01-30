import unittest
from hello import hello_simple

class TestHelloSimple(unittest.TestCase):
    
    def test_hello_simple(self):
        """Test the hello_simple function."""
        expected = "Hello, I'm simple!"
        result = hello_simple()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()