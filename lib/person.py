#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

        
    approved_jobs = ["Teacher", "Engineer", "Doctor", "Artist"]

    def __init__(self, name, job):
        if not 1 <= len(name) <= 25:
            print("Name must be string between 1 and 25 characters.")
        if not isinstance(name, str):
            print("Name must be a string.")
        if job not in Person.approved_jobs:
            print("Job must be in list of approved jobs.")
        self.name = name.title()
        self.job = job

