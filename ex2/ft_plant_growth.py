class Plant:
    def __init__(self, name, height, growPerDay, old):
        self.name = name
        self.height = height
        self.growPerDay = growPerDay
        self.old = old

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.old} days old")

    def grow(self, grow):
        self.grow = grow

    def age(self, days):
        count = 1
        aux = self.height
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        while (count <= days):
            self.height += self.growPerDay
            self.old += 1
            print(f"=== Day {count} ===")
            print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
            count += 1
        print(f"Growth this week: {self.height - aux:.1f} cm")


def main():
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 0.8, 30)
    plant1.age(7)


if __name__ == "__main__":
    main()
