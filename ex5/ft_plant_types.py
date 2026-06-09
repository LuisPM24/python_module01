class Plant:
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

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")

    def grow(self) -> None:
        self.height += self.growPerDay

    def age(self, days: int) -> None:
        count = 1
        while (count <= days):
            self.grow()
            self.old += 1
            count += 1


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


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, growPerDay, old)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")

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
