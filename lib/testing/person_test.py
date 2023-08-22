#!/usr/bin/env python3

import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_name_validation(self):
        person = Person("Alice", "Engineer")
        # Test name length and title case conversion
        self.assertEqual(person.name, "Alice")
        # Test empty name
        person_empty_name = Person("", "Doctor")
        self.assertIsNone(person_empty_name.name)

    def test_job_validation(self):
        person_valid_job = Person("Bob", "Doctor")
        # Test approved job
        self.assertEqual(person_valid_job.job, "Doctor")
        # Test job not in approved list
        person_invalid_job = Person("Charlie", "Musician")
        self.assertIsNone(person_invalid_job.job)

if __name__ == '__main__':
    unittest.main()

