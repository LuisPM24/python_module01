class Plant:
    def __init__(self, name, height, growPerDay, old):
        self.name = name
        self.height = height
        self.growPerDay = growPerDay
        self.old = old

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")

    def grow(self, grow):
        self.grow = grow

    def set_height(self, height):
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm")

    def set_age(self, old):
        if (old < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.old = old
            print(f"Age updated: {self.old} days")

    def get_height(self):
        print(f"{self.height}cm")

    def get_age(self):
        print(f"{self.old} days")

    def age(self, days):
        count = 1
        aux = self.height
        self.show()
        while (count <= days):
            self.height += self.growPerDay
            self.old += 1
            print(f"=== Day {count} ===")
            self.show()
            count += 1
        print(f"Growth this week: {self.height - aux:.1f} cm")


class Flower(Plant):
    pass

    def __init__(self, name, height, growPerDay, old, color):
        super().__init__(name, height, growPerDay, old)
        self.color = color
        self.hasBloomed = False

    def bloom(self):
        self.hasBloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.hasBloomed):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    pass

    def __init__(self, name, height, growPerDay, old, trunk_diameter):
        super().__init__(name, height, growPerDay, old)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    pass

    def __init__(self, name, height, growPerDay, old, harvest_season,
                 nutritional_value):
        super().__init__(name, height, growPerDay, old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self, days):
        super().age(days)
        self.nutritional_value += days

    def grow(self, grow):
        super().grow(grow)
        self.nutritional_value += grow


def main():
    flower1 = Flower("Rose", 15.0, 0.8, 10, "red")
    tree1 = Tree("Oak", 200.0, 0.3, 365, 5.0)
    vegetable1 = Vegetable("Tomato", 5.0, 1, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1.show()
    print("[asking the rose to bloom]")
    flower1.bloom()
    flower1.show()
    print("\n=== Tree")
    tree1.show()
    print("[asking the oak to produces shade]")
    tree1.produce_shade()
    print("\n=== Vegetable")
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    vegetable1.grow(20)
    vegetable1.show()


if __name__ == "__main__":
    main()
