import time


class CoffeeMachine:
    max_water = 1000
    max_beans = 500
    max_milk = 500

    def __init__(self, water=0, beans=0, milk=0):
        self.__water_level = water
        self.__coffee_beans = beans
        self.__milk_level = milk
        self.__waste_counter = 0

    @property
    def get_status(self):
        return (f"Количество воды: {self.__water_level} мл\n"
                f"Количество зёрен: {self.__coffee_beans} г\n"
                f"Количество молока: {self.__milk_level} мл\n"
                f"Количество отходов: {self.__waste_counter} порций")

    def add_water(self, amount):
        if amount <= 0:
            raise ValueError("Ошибка: можно добавлять только положительное количество воды")

        if self.__water_level + amount > self.max_water:
            raise ValueError(f"Ошибка: суммарный объём воды {self.__water_level + amount} мл")

        self.__water_level += amount

    def add_beans(self, amount):
        if amount <= 0:
            raise ValueError("Ошибка: можно добавлять только положительное количество зёрен")

        if self.__coffee_beans + amount > self.max_beans:
            raise ValueError(f"Ошибка: суммарный объём зёрен {self.__coffee_beans + amount} г")

        self.__coffee_beans += amount

    def add_milk(self, amount):
        if amount <= 0:
            raise ValueError("Ошибка: можно добавлять только положительное количество молока")

        if self.__milk_level + amount > self.max_milk:
            raise ValueError(f"Ошибка: суммарный объём молока {self.__milk_level + amount} мл")

        self.__milk_level += amount

    def clean_machine(self):
        self.__waste_counter = 0
        return "Успешная очистка контейнера отходов!"

    def make_coffee(self):
        if self.__waste_counter >= 5:
            raise ValueError("Ошибка: очистите контейнер отходов")

        print("╔════════════════════════════════════════════════╗\n"
              "|                 ВЫБОР НАПИТКА                  |\n"
              "╠════════════════════════════════════════════════╣\n"
              "|  [1] Эспрессо                                  |\n"
              "|      (50 мл воды | 10 г зёрен)                 |\n"
              "|  [2] Американо                                 |\n"
              "|      (150 мл воды | 15 г зёрен)                |\n"
              "|  [3] Капучино                                  |\n"
              "|      (100 мл воды | 15 г зёрен | 50 мл молока) |\n"
              "|  [4] Вернуться в главное меню                  |\n"
              "╚════════════════════════════════════════════════╝")

        while True:
            choice = int(input("Выберите напиток (1-4): "))

            if choice == 1:
                if self.__water_level < 50:
                    raise ValueError("Ошибка: недостаточное количество воды")
                if self.__coffee_beans < 10:
                    raise ValueError("Ошибка: недостаточное количество зёрен")

                self.__water_level -= 50
                self.__coffee_beans -= 10
                break

            elif choice == 2:
                if self.__water_level < 150:
                    raise ValueError("Ошибка: недостаточное количество воды")
                if self.__coffee_beans < 15:
                    raise ValueError("Ошибка: недостаточное количество зёрен")

                self.__water_level -= 150
                self.__coffee_beans -= 15
                break

            elif choice == 3:
                if self.__water_level < 100:
                    raise ValueError("Ошибка: недостаточное количество воды")
                if self.__coffee_beans < 15:
                    raise ValueError("Ошибка: недостаточное количество зёрен")
                if self.__milk_level < 50:
                    raise ValueError("Ошибка: недостаточное количество молока")

                self.__water_level -= 100
                self.__coffee_beans -= 15
                self.__milk_level -= 50
                break

            elif choice == 4:
                print("Возвращаемся в меню...")
                return

            else:
                print("Ошибка: выберите число от 1 до 4")
                continue

        self.__waste_counter += 1

        print("\n")
        for percent in range(0, 101, 20):
            bar = "█" * (percent // 10) + "-" * (10 - percent // 10)
            print(f"\rГотовим кофе... [{bar}] {percent}%", end="")
            time.sleep(0.3)
        print("\nГотово, осторожно, горячо!\n")


def run():
    coffee = CoffeeMachine()

    while True:
        print("\n╔═════════════════════════════════════════╗")
        print("|           COFFEE MACHINE CLI            |")
        print("╠═════════════════════════════════════════╣")
        print("|  [1] Посмотреть статус ресурсов         |")
        print("|  [2] Приготовить кофе                   |")
        print("|  [3] Добавить воду                      |")
        print("|  [4] Добавить зёрна                     |")
        print("|  [5] Добавить молоко                    |")
        print("|  [6] Очистить контейнер отходов         |")
        print("|  [7] Выход                              |")
        print("╚═════════════════════════════════════════╝")

        try:
            command = int(input("Выберите команду (1-7): "))

            if command == 1:
                print("\n" + coffee.get_status)

            elif command == 2:
                coffee.make_coffee()

            elif command == 3:
                amount_water = int(input("Сколько добавить воды? "))
                coffee.add_water(amount_water)
                print("Вода успешно добавлена!")

            elif command == 4:
                amount_beans = int(input("Сколько добавить зёрен? "))
                coffee.add_beans(amount_beans)
                print("Зёрна успешно добавлены!")

            elif command == 5:
                amount_milk = int(input("Сколько добавить молока? "))
                coffee.add_milk(amount_milk)
                print("Молоко успешно добавлено!")

            elif command == 6:
                print(coffee.clean_machine())

            elif command == 7:
                print("До свидания, ждём вас снова!")
                break

            else:
                print("Неизвестная команда, введите число от 1 до 7")

        except ValueError as e:
            print(f"\n[!] {e}")


if __name__ == "__main__":
    run()
