#!/usr/bin/env python3
import unittest
from dog import Dog
from person import Person


class TestDog(unittest.TestCase):
    def test_name_validation(self):
        dog = Dog("Fido", "Labrador")
        # Test name length
        self.assertEqual(dog.name, "Fido")
        # Test empty name
        dog_empty_name = Dog("", "Poodle")
        self.assertIsNone(dog_empty_name.name)

    def test_breed_validation(self):
        dog_valid_breed = Dog("Rex", "Husky")
        # Test approved breed
        self.assertEqual(dog_valid_breed.breed, "Husky")
        # Test breed not in approved list
        dog_invalid_breed = Dog("Buddy", "Dachshund")
        self.assertIsNone(dog_invalid_breed.breed)

if __name__ == '__main__':
    unittest.main()
