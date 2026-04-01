import unittest
from contacts_manager import validate_phone

class TestContactManager(unittest.TestCase):
    
    def test_phone_validation_valid(self):
        self.assertTrue(validate_phone("9876543210"))
        
    def test_phone_validation_invalid_short(self):
        self.assertFalse(validate_phone("123"))

    def test_phone_validation_invalid_alpha(self):
        self.assertFalse(validate_phone("abcdefghij"))

if __name__ == "__main__":
    unittest.main()
