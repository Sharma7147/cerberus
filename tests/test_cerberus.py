import unittest
from cerberus.core import generate_passwords

class TestCerberus(unittest.TestCase):
    def test_generation(self):
        pwds = generate_passwords(
            first="john",
            last="ahmed",
            usernames=["johnny"],
            emails=["john@example.com"],
            pets=["bruno"],
            numbers=["123", "2025"],
            dob="2001-07-15",
            limit=2000
        )
        self.assertGreater(len(pwds), 500)
        self.assertIn("john123", pwds)
        self.assertIn("ahmed2025", pwds)

if __name__ == "__main__":
    unittest.main()
