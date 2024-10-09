from book import Book
from calculator import Calculator
from car import Car

def main():
    harry_potter_1 = Book('Harry Potter y la Piedra Filosofal', 'J. K. Rowling', 'Salamanca')
    harry_potter_2 = Book('Harry Potter y la Camara Secreta', 'J. K. Rowling', 'Salamanca')
    
    harry_potter_1.add_copies(5)
    
    # print(harry_potter_1.get_data())
    # print(harry_potter_2.get_data())
    # print(harry_potter_1.title)
    # print(Book.get_count())
    # harry_potter_1.count = 10
    # print(harry_potter_1.copies)

    # res = Calculator.circle_area(2.5)
    # print(res)
    car = Car('Renault', 'Logan', 2016)
    print(car)




if __name__ == '__main__':
    main()
