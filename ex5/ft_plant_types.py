class Plant:
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int) -> None:
        self._name = name
        self._growPerDay = growPerDay
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if (old < 0):
            print(f"{self._name}: Error, age can't be negative")
            self._old = 0
        else:
            self._old = old

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._old = new_age
            print(f"Age updated: {new_age} days")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._old} days old")

    def grow(self) -> None:
        self._height += self._growPerDay

    def age(self, days: int) -> None:
        count = 1
        while (count <= days):
            self.grow()
            self._old += 1
            count += 1


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int, color: str) -> None:
        super().__init__(name, height, growPerDay, old)
        self._color = color
        self._hasBloomed = False

    def bloom(self) -> None:
        self._hasBloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if (self._hasBloomed):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, growPerDay, old)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, growPerDay, old)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    flower1 = Flower("Rose", 15.0, 0.8, 10, "red")
    tree1 = Tree("Oak", 200.0, 0.3, 365, 5.0)
    vegetable1 = Vegetable("Tomato", 5.0, 2.1, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1.show()
    print("[asking the rose to bloom]")
    flower1.bloom()
    flower1.show()
    print("\n=== Tree")
    tree1.show()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("\n=== Vegetable")
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    vegetable1.age(20)
    vegetable1.show()


if __name__ == "__main__":
    main()
