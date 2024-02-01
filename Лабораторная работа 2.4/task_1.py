class Devices:
    """Базовый класс Устройства"""
    def __init__(self, name: str, version: float, country: str, year_of_release: int, company: str):
        self.name = name  # Название устройства
        self._version = version  # Версия устройства /
        # непубличный в связи с тем, что для него нужно сделать свойство проверки
        self.country = country  # Страна производитель
        self._year = year_of_release  # Год выпуска /
        # непубличный в связи с тем, что для него нужно сделать свойство проверки
        self.company = company  # Компания

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, new_version):
        if not isinstance(new_version, float):
            raise TypeError
        elif new_version <= 0.0:
            raise ValueError
        else:
            self._version = new_version

    @property
    def year_of_release(self):
        return self._year

    @year_of_release.setter
    def year_of_release(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError
        elif new_year <= 0:
            raise ValueError
        else:
            self._year = new_year

    def next_version_and_year(self, new_vers: float, new_year: int):  # Метод для установки новой версии и
        # года устройства
        if isinstance(new_year, int) and isinstance(new_vers, float):
            if new_vers > self._version and new_year >= self._year:
                self._version = new_vers
                self._year = new_year
            else:
                raise ValueError
        else:
            raise TypeError

    def __str__(self):
        return (f"Устройство - {self.name}; "
                f"Версия - {self.version}; "
                f"Страна производитель - {self.country}; "
                f"Год выпуска - {self.year_of_release} год; "
                f"Компания - {self.company};")

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"name={self.name!r}, " \
               f"version={self.version!r}, " \
               f"country={self.country!r}, " \
               f"year_of_release={self.year_of_release!r}, " \
               f"company={self.company!r})"


class Screen(Devices):
    """Устройство - Монитор"""
    def __init__(self, name: str, version, country: str, year_of_release: int, company: str, color: str, model: str,
                 weight: float, warranty: int):
        super().__init__(name, version, country, year_of_release, company)
        self.color = color  # Цвет монитора
        self.model = model  # Модель монитора
        self._weight = weight  # Вес монитора (в килограмах) /
        # непубличный в связи с тем, что для него нужно сделать свойство проверки
        self._warranty = warranty  # Гарантия на монитор (в месяцах) /
        # непубличный в связи с тем, что для него нужно сделать свойство проверки

    @property
    def warranty(self):
        return self._warranty

    @warranty.setter
    def warranty(self, new_warranty):
        if not isinstance(new_warranty, int):
            raise TypeError
        elif new_warranty < 0:
            raise ValueError
        else:
            self._warranty = new_warranty

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if not isinstance(new_weight, float):
            raise TypeError
        elif new_weight < 0.0:
            raise ValueError
        else:
            self._weight = new_weight

    def __str__(self):
        return f"{super().__str__()} Цвет - {self.color}; Модель - {self.model};" \
               f" Вес - {self.weight} кг.; Гарантия - {self.warranty} мес.;"

    def next_version_and_year(self, new_vers: float, new_year: int):
        super().next_version_and_year(new_vers, new_year)  # т к тут так же используется версия и год выпуска,
        # что бы не повторятся, перегружаю метод с базового класса

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"name={self.name!r}, " \
               f"version={self.version!r}, " \
               f"country={self.country!r}, " \
               f"year_of_release={self.year_of_release!r}, " \
               f"company={self.company!r}, " \
               f"color={self.color!r}, " \
               f"model={self.model!r}, " \
               f"weight={self.weight!r}, " \
               f"warranty={self.warranty!r})"


if __name__ == "__main__":
    pass
