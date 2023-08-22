#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            self.breed = None


