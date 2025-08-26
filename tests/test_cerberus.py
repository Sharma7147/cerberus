import unittest
from cerberus.core import generate_passwords


class TestCerberus(unittest.TestCase):
    def test_basic_generation(self):
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
        self.assertGreater(len(pwds), 500)
        self.assertIn("john123", pwds)
        self.assertIn("ahmed2025", pwds)

    def test_min_max_length(self):
        pwds = generate_passwords(
            first="test",
            last="case",
            usernames=["tc"],
            emails=[],
            pets=[],
            numbers=["99"],
            dob="",
            min_len=10,
            max_len=12,
            limit=500
        )
        # All passwords should respect length bounds
        self.assertTrue(all(10 <= len(p) <= 12 for p in pwds))

    def test_charset_requirements(self):
        pwds = generate_passwords(
            first="alpha",
            last="beta",
            usernames=[],
            emails=[],
            pets=[],
            numbers=["123"],
            dob="",
            need_digit=True,
            need_upper=True,
            need_symbol=True,
            limit=500
        )
        # Ensure every password respects charset requirements
        for pw in pwds:
            self.assertTrue(any(c.isdigit() for c in pw), f"Missing digit in {pw}")
            self.assertTrue(any(c.isupper() for c in pw), f"Missing uppercase in {pw}")
            self.assertTrue(any(c in "@_-.$!#%&*?" for c in pw), f"Missing symbol in {pw}")


if __name__ == "__main__":
    unittest.main()
