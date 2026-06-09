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
        aux = self.height
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        while (count <= days):
            self.grow()
            self.old += 1
            print(f"=== Day {count} ===")
            self.show()
            count += 1
        print(f"Growth this week: {self.height - aux:.1f} cm")


def main() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 0.8, 30)
    plant1.age(7)


if __name__ == "__main__":
    main()
