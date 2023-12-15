import doctest


class Chocolate:
    """описание шоколада"""
    def __init__(self, variety: str, cooking_method: str, shape: str):
        """
        Виды шоколада по способу производства

        :param variety: разновидность шоколада
        :param cooking_method: способ приготовления
        :param shape: форма шоколада
        :self.filing: начинка шоколада

        Примеры:
        >>> chocolate = Chocolate('молочный', 'пористый', 'плиточный')
        """
        self.variety = variety
        self.cooking_method = cooking_method
        self.shape = shape
        self.filing = ""

    def check_chocolate_value(self, value):
        """
        Функция проверяющая  тип данных

        :param value: вызываем атрибут для проверки типа данных
        :raise TypeError: если атрибут не является типом str, возврощаем ошибку
        :raise ValueError: если атрибут не состоит только из букв, возврощаем ошибку

        Примеры:
        >>> chocolate = Chocolate('молочный', 'пористый', 'плиточный')
        >>> chocolate.check_chocolate_value(chocolate.shape)
        """
        if not isinstance(value, str):
            raise TypeError("разновидность/способ приготовления/форма/начинка должен/на быть типа str")
        if not value.isalpha():
            raise ValueError("разновидность/способ приготовления/форма/начинка должен/на состоять только из букв")

    def adding_the_filling(self, filling: str):
        """
        Функция добавляющая начинку

        :param filling: Вид добовляемой начинки
        :chocolate.adding_the_filling(): добовляем начинку
        :chocolate.check_chocolate_value(filling): проверяем состоит ли начинка из типа str и только букв

        Примеры:
        >>> chocolate = Chocolate('молочный', 'пористый', 'плиточный')
        >>> chocolate.adding_the_filling("орехами")
        >>> chocolate.check_chocolate_value(chocolate.filing)
        >>> print( f"{chocolate.variety} шоколад с {chocolate.filing}")
        молочный шоколад с орехами
        """
        self.filing = filling


class Animal:
    """описание животного"""
    def __init__(self, name: str, age: int, gender: str):
        """
        Вид животного и его некоторые характеристики

        :param name: Имя животного
        :param age: Возраст животного
        :param gender: Гендер животного
        :self.foodd: Вид еды
        :self.sleepp: Продолжительность сна

        Примеры:
        >>> animal = Animal("Собака", 2, "Самец")
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.foodd = ""
        self.sleepp = 0

    def eat(self, food: str):
        """
        Функция принимает на вход пищу которую животное будет есть

        :param food: Еда для животного
        :animal.eat("корм"): передаем еду для собаки
        :animal.check_animal_value_str(animal.foodd): проверям состоит ли еда из типа str и только букв

        Примеры:
        >>> animal = Animal("Собака", 2, "Самец")
        >>> animal.eat("корм")
        >>> animal.check_animal_value_str(animal.foodd)
        >>> print(f"{animal.name} будет есть {animal.foodd}")
        Собака будет есть корм
        """
        self.foodd = food

    def sleep(self, duration: (int, float)):
        """
        Функция описывающая продолжительность сна

        :param duration: Продолжительность сна (в часах)
        :animal.sleep(3): присваиваем количество часов сна
        :animal.check_animal_value_int_float(animal.sleepp): проверяем состят ли часы из положительных чисел

        Примеры:
        >>> animal = Animal("Собака", 2, "Самец")
        >>> animal.sleep(3)
        >>> animal.check_animal_value_int_float(animal.sleepp)
        >>> print(f"{animal.name} проспала {animal.sleepp} часа")
        Собака проспала 3 часа
        """
        self.sleepp = duration

    def check_animal_value_str(self, value: str):
        """
        Функция проверяющая  тип данных для строчных атрибутов

        :param value: вызываем атрибут для проверки типа данных
        :raise TypeError: если атрибут не является типом str, возврощаем ошибку
        :raise ValueError: если атрибут не состоит только из букв, возврощаем ошибку

        Примеры:
        >>> animal = Animal("Собака", 2, "Самец")
        >>> animal.check_animal_value_str(animal.gender)
        """
        if not isinstance(value, str):
            raise TypeError(" имя/гендер животного/еда должно/ен/на быть типа str")
        if not value.isalpha():
            raise ValueError("имя/гендер животного/еда должно/ен/на состоять только из букв")

    def check_animal_value_int_float(self, value):
        """
                Функция проверяющая  тип данных для  числовых атрибутов

                :param value: вызываем атрибут для проверки типа данных
                :raise TypeError: если атрибут не является типом int/float, возврощаем ошибку
                :raise ValueError: если атрибут не состоит из положительных чисел, возврощаем ошибку

                Примеры:
                >>> animal = Animal("Собака", 2, "Самец")
                >>> animal.check_animal_value_int_float(animal.age)
                """
        if not isinstance(value, (int, float)):
            raise TypeError("возраст/продолжительность сна должен/на быть типа int/float")
        if value < 0:
            raise ValueError("возраст/продолжительность сна должен/на состоять из положительного числа")


class House:
    """описание дома"""
    def __init__(self, street: str, number: int):
        """
        свойства дома

        :param street: улица дома
        :param number: номер дома
        :age: возраст дома

        :raise TypeError: если улица не является типом str, возврощаем ошибку
        :raise ValueError: если улица не состоит только из букв, возврощаем ошибку

        Примеры:
        >>> house = House("Пушкина", 47)
        """
        self.street = street
        self.number = number
        self.age = 0
        if not isinstance(street, str):
            raise TypeError("улица должна быть типа str")
        if not street.isalpha():
            raise ValueError("улица должна состоять только из букв")

    def build(self):
        """
        Функция постройки дома

        Примеры:
        >>> house = House("Пушкина", 47)
        >>> print(f"Дом на улице {house.street} под номером {house.number} построен")
        Дом на улице Пушкина под номером 47 построен
        """
        ...

    def reconstruction(self):
        """
        Функция реконструкции дома

        Примеры:
        >>> house = House("Пушкина", 47)
        >>> print(f"Дом на улице {house.street} под номером {house.number} был реконструирован")
        Дом на улице Пушкина под номером 47 был реконструирован
        """
        ...

    def age_of_house(self, year: int):
        """
        Функция определяющая возраст дома
        :param year: показывает возраст дома
        :house.age_of_house(5): присваеваем возраст дома
        :house.check_house_value(house.age): проверяем являеться ли возраст положительным числом

        Примеры:
        >>> house = House("Пушкина", 47)
        >>> house.age_of_house(5)
        >>> house.check_house_value(house.age)
        >>> print(f"возраст дома {house.age} лет")
        возраст дома 5 лет
        """
        self.age += year

    def check_house_value(self, value):
        """
                Функция проверяющая  тип данных для  атрибутов

                :param value: вызываем атрибут для проверки типа данных
                :raise TypeError: если атрибут не является типом int/float, возврощаем ошибку
                :raise ValueError: если атрибут не состоит из положительных чисел, возврощаем ошибку

                Примеры:
                >>> house = House("Пушкина", 47)
                >>> house.check_house_value(house.number)
                """
        if not isinstance(value, (int, float)):
            raise TypeError("улица/возраст должна/ен быть типа int/float")
        if value < 0:
            raise ValueError("улица/возраст должна/ен состоять из положительного числа")


if __name__ == "__main__":
    doctest.testmod()
    pass
