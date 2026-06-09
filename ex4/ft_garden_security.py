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
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        while (count <= days):
            self.grow()
            self.old += 1
            count += 1


def main() -> None:
    plant1 = Plant("Rose", 15.0, 0.8, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1.show()
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-1)
    plant1.set_age(-1)
    print()
    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
