class Plant:
    def __init__(self, name: str, height: float,
                 growPerDay: float, old: int) -> None:
        self.name = name
        self.height = height
        self.growPerDay = growPerDay
        self.old = old

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")

    def grow(self) -> None:
        self.height += self.growPerDay

    def age(self, days: int) -> None:
        count = 1
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        while (count <= days):
            self.grow()
            self.old += 1
            count += 1


def main() -> None:
    plant1 = Plant("Rose", 25.0, 0.8, 30)
    plant2 = Plant("Oak", 200.0, 0.2, 365)
    plant3 = Plant("Cactus", 5.0, 0.3, 90)
    plant4 = Plant("Sunflower", 80.0, 0.4, 45)
    plant5 = Plant("Fern", 15.0, 0.1, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
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
