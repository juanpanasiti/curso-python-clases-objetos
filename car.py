from datetime import datetime


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def age(self):
        return datetime.now().year - self.year

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'
