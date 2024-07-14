class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):   # должен возвращать строку
        return f'Название: {self.name} Количество этажей: {self.number_of_floors}'

    def __len__(self):   # должен возвращать кол-во этажей здания
        return self.number_of_floors

    def __del__(self):   # будет срабатывать деструктор
        print(f'Ну вот и все, с {self.name} интерпретатор заканчивает свою работу')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))