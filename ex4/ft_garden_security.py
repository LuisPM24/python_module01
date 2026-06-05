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


def main():
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
