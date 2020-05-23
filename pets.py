class Animals():

    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound

    def feed(self):
        self.state = "Кормить"


class Geese(Animals):
    def pic_up_eggs(self):
        self.state = "Собрать яйца"


class Hen(Geese, Animals):
    pass


class Cow(Animals):
    def get_milk(self):
        self.state = "Доить"


class Goat(Cow, Animals):
    pass


class Sheep(Animals):
    def shave(self):
        self.state = "Стричь"


class Duck(Geese, Animals):
    pass


cow = Cow(name='Манька', weight=430, sound='Му-му')
duck = Duck(name='Кряква', weight=15, sound='Кря-кря')
sheep1 = Sheep(name='Барашек', weight=140, sound='бе-бе')
sheep2 = Sheep(name='Кудрявый', weight=155, sound='бе-бе')
hen1 = Hen(name='Ко-Ко', weight=10, sound='кур-кур')
hen2 = Hen(name='Кукареку', weight=10, sound='кур-кур')
goat1 = Goat(name='Рога', weight=90, sound='Ме-ме')
goat2 = Goat(name='Копыта', weight=80, sound='Ме-ме')
goose1 = Geese(name='Серый', weight=20, sound='шшшшшш')
goose2 = Geese(name='Белый', weight=20, sound='шшшшшш')



pets =["сow", "duck", "sheep1", "sheep2", "hen1", "hen2", "goat1", "goat2", "goose1", "goose2"]
print(max(pets))
