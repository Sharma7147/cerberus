import unittest
from cerberus.core import generate_passwords

class TestCerberus(unittest.TestCase):
    def test_generation_basic(self):
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
        # Basic sanity checks
        self.assertGreater(len(pwds), 0, "No passwords generated")
        # Presence checks for common combos
        self.assertIn("john123", pwds, "Expected 'john123' in generated passwords")
        self.assertIn("ahmed2025", pwds, "Expected 'ahmed2025' in generated passwords")

    def test_min_max_length(self):
        pwds = generate_passwords(
            first="test",
            last="case",
            usernames=["tc"],
            emails=[],
            pets=[],
            numbers=["99"],
            dob="",
            min_len=6,
            max_len=12,
            limit=500
        )
        # All passwords should respect length bounds
        self.assertTrue(all(6 <= len(p) <= 12 for p in pwds), "Found password outside min/max bounds")

if __name__ == "__main__":
    unittest.main()
