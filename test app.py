import unittest
from app import greet  # This assumes app.py and test_app.py are in the same directory

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice! Welcome to Python and Git.")
        self.assertEqual(greet("Bob"), "Hello, Bob! Welcome to Python and Git.")
        self.assertNotEqual(greet("Eve"), "Hi Eve!")

if __name__ == "__main__":
    unittest.main()
