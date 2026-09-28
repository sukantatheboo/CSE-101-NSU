class Smartphone:
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        print("fully charged")


# my_phone = Smartphone("Apple", 15)
# print(f"Battery before: {my_phone.battery_level}")
# my_phone.charge()
# print(f"Battery after: {my_phone.battery_level}")


class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Vexana took {damage} damage!")

    def heal(self, amount):
        self.hp += amount


# Test your code:
my_hero = Hero("Vexana", 500)
print(f"Starting HP: {my_hero.hp}")
my_hero.take_damage(150)
print(f"HP after attack: {my_hero.hp}")
my_hero.heal(50)
print(f"HP after healing: {my_hero.hp}")
