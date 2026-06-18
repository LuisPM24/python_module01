class Plant:
    class Stats:
        def __init__(self) -> None:
            self._growCalls = 0
            self._ageCalls = 0
            self._showCalls = 0
            self._isTree = False
            self._shadeCalls = 0

        def incrementGrow(self) -> None:
            self._growCalls += 1

        def incrementAge(self) -> None:
            self._ageCalls += 1

        def incrementShow(self) -> None:
            self._showCalls += 1

        def incrementShade(self) -> None:
            self._shadeCalls += 1

        def statistics(self) -> None:
            print(f"Stats: {self._growCalls} grow, ", end="")
            print(f"{self._ageCalls} age, {self._showCalls} show")
            if (self._isTree):
                print(f" {self._shadeCalls} shade")

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
        self._stats = Plant.Stats()

    @classmethod
    def create_anom(cls, name: str = "Unknown plant", height: float = 0.0,
                    growPerDay: float = 0.0, old: int = 0) -> 'Plant':
        return cls(name, height, growPerDay, old)

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

    @staticmethod
    def check_age(old: int) -> bool:
        return (365 < old)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._old} days old")
        self._stats.incrementShow()

    def grow(self) -> None:
        self._height += self._growPerDay
        self._stats.incrementGrow()

    def age(self, days: int) -> None:
        count = 1
        while (count <= days):
            self._height += self._growPerDay
            self._old += 1
            count += 1
        self._stats.incrementAge()


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int, color: str) -> None:
        super().__init__(name, height, growPerDay, old, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, growPerDay, old)
        self._stats._isTree = True
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._stats.incrementShade()

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
    flower1 = Flower("Rose", 15.0, 8, 10, "red")
    tree1 = Tree("Oak", 200.0, 1.0, 365, 5.0)
    seed1 = Seed("Sunflower", 80.0, 1.43, 45, "yellow")
    anonymous1 = Plant.create_anom()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", end="")
    print(f"{Plant.check_age(30)}")
    print("Is 400 days more than a year? -> ", end="")
    print(f"{Plant.check_age(400)}")
    print("\n=== Flower")
    flower1.show()
    print("[statistics for Rose]")
    flower1._stats.statistics()
    print("[asking the rose to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1.show()
    flower1._stats.statistics()
    print("\n=== Tree")
    tree1.show()
    print("[statistics for Oak]")
    tree1._stats.statistics()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    tree1._stats.statistics()
    print("\n=== Seed")
    seed1.show()
    print("[make sunflower grow, age and bloom]")
    seed1.grow()
    seed1.age(20)
    seed1.bloom()
    seed1.show()
    print("[statistics for Sunflower]")
    seed1._stats.statistics()
    print("\n=== Anonymous")
    anonymous1.show()
    print("[statistics for Unknown plant]")
    anonymous1._stats.statistics()


if __name__ == "__main__":
    main()
