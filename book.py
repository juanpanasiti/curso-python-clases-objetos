class Book:
    count = 0  # Atributo de clase

    def __init__(self, title, author, editorial=''):
        self.title = title  # Atributo de instancia u objeto
        self.author = author  # Atributo de instancia u objeto
        self.editorial = editorial  # Atributo de instancia u objeto
        self.count = 1

        # Book.count += 1

    @property
    def copies(self):
        return self.count

    def get_data(self):  # Metodo de instancia u objeto
        return f'{self.title} - {self.author} ({self.editorial or 'sin editorial'}) {self.count}/{Book.count}'
    
    @classmethod
    def get_count(cls):
        return cls.count


    def add_copies(self, quantity=1):
        self.count += quantity
        Book.count += quantity

