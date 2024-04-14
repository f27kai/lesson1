class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def Name(self):
        print(f"Name: {self.name}")

    def health(self):
         self.health_points *= 2

    def __str__(self):
        return (f"Nickname: {self.nickname}\n"
                f"Superpower: {self.superpower}\n"
                f"HEALTH POINTS: {self.health_points}\n")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Ruslan", "Roka", "athlete", 100, "Элементарно, мой дорогой Ватсон")
hero.Name()
print(hero)

print("Before:", hero.health_points)
hero.health()
print("After:", hero.health_points)
print(len(hero))
