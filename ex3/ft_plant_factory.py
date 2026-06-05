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


def main():
    plant1 = Plant("Rose", 25.0, 0.8, 30)
    plant2 = Plant("Oak", 200.0, 0.2, 365)
    plant3 = Plant("Cactus", 5.0, 0.5, 90)
    plant4 = Plant("Sunflower", 80.0, 0.6, 45)
    plant5 = Plant("Fern", 15.0, 0.1, 120)
    print("=== Plant Factory Output ===\nCreated: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    main()
