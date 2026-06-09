class Plant:
    class Stats:
        def __init__(self) -> None:
            self.growCalls = 0
            self.ageCalls = 0
            self.showCalls = 0
            self.isTree = False
            self.shadeCalls = 0

        def incrementGrow(self) -> None:
            self.growCalls += 1

        def incrementAge(self) -> None:
            self.ageCalls += 1

        def incrementShow(self) -> None:
            self.showCalls += 1

        def incrementShade(self) -> None:
            self.shadeCalls += 1

        def statistics(self) -> None:
            print(f"Stats: {self.growCalls} grow, ", end="")
            print(f"{self.ageCalls} age, {self.showCalls} show")
            if (self.isTree):
                print(f" {self.shadeCalls} shade")

    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int) -> None:
        self.name = name
        self.growPerDay = growPerDay
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            self.height = 0.0
        else:
            self.height = height
        if (old < 0):
            print(f"{self.name}: Error, age can't be negative")
            self.old = 0
        else:
            self.old = old
        self.stats = Plant.Stats()

    @classmethod
    def create_anom(cls, name: str = "Unknown plant", height: float = 0.0,
                    growPerDay: float = 0.0, old: int = 0) -> 'Plant':
        return cls(name, height, growPerDay, old)

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.old = new_age
            print(f"Age updated: {new_age} days")

    @staticmethod
    def check_age(old: int) -> bool:
        return (365 < old)

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        self.stats.incrementShow()

    def grow(self) -> None:
        self.height += self.growPerDay
        self.stats.incrementGrow()

    def age(self, days: int) -> None:
        count = 1
        while (count <= days):
            self.height += self.growPerDay
            self.old += 1
            count += 1
        self.stats.incrementAge()


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int, color: str) -> None:
        super().__init__(name, height, growPerDay, old)
        self.color = color
        self.hasBloomed = False

    def bloom(self) -> None:
        self.hasBloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.hasBloomed):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int, color: str) -> None:
        super().__init__(name, height, growPerDay, old, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, growPerDay, old)
        self.stats.isTree = True
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.incrementShade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, growPerDay, old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


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
    flower1.stats.statistics()
    print("[asking the rose to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1.show()
    flower1.stats.statistics()
    print("\n=== Tree")
    tree1.show()
    print("[statistics for Oak]")
    tree1.stats.statistics()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    tree1.stats.statistics()
    print("\n=== Seed")
    seed1.show()
    print("[make sunflower grow, age and bloom]")
    seed1.grow()
    seed1.age(20)
    seed1.bloom()
    seed1.show()
    print("[statistics for Sunflower]")
    seed1.stats.statistics()
    print("\n=== Anonymous")
    anonymous1.show()
    print("[statistics for Unknown plant]")
    anonymous1.stats.statistics()


if __name__ == "__main__":
    main()
