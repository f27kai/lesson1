class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def health(self):
         self.health_points *= 2
         self.fly = True


    def say_catchphrase(self):
        return f"{self.name}: '{self.catchphrase}'"


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = True


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False


class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = True

class Villain(SpaceHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2


air_hero = AirHero("Воздушный герой", "Airman", "летать", 100, "В небе мы свободны!", 10)
earth_hero = EarthHero("Земной герой", "Earthman", "земля", 120, "Земля - наш дом!", 15)
space_hero = SpaceHero("Космический герой", "Spaceman", "космос", 150, "Мы встретимся в космосе!", 20)
villain = Villain("Злодей", "Darklord", "зло", 200, "Тьма владеет мной!", 25)


air_hero.health()
earth_hero.health()
space_hero.health()
villain.health()

print("Air Hero Fly Status:", air_hero.fly)
print("Earth Hero Fly Status:", earth_hero.fly)
print("Space Hero Fly Status:", space_hero.fly)
print("Villain Fly Status:", villain.fly)

print("Air Hero Catchphrase:", air_hero.say_catchphrase())
print("Earth Hero Catchphrase:", earth_hero.say_catchphrase())
print("Space Hero Catchphrase:", space_hero.say_catchphrase())
print("Villain Catchphrase:", villain.say_catchphrase())

print("Villain Gen X Method:", villain.gen_x())
print("Villain Critical Damage:", villain.crit(10))
