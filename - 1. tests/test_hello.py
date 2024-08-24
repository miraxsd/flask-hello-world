import unittest

def hello(name):
    return f"Hello, {name}!"

class TestHelloFunction(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")
        self.assertEqual(hello("Alice"), "Hello, Alice!")
        self.assertEqual(hello("Bob"), "Hello, Bob!")
        
    def test_hello_empty(self):
        self.assertEqual(hello(""), "Hello, !")

if __name__ == '__main__':
    unittest.main()