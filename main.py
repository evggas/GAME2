from abc import ABC,abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "удар мечом!"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука!"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        
        weapon_names = {
            "Sword": "меч",
            "Bow": "лук"
        }
        weapon_name = weapon_names.get(self.weapon.__class__.__name__, self.weapon.__class__.__name__)
        print(f"{self.name} выбрал {weapon_name}")

    def attack(self):
        if self.weapon:
            print(f"{self.name} наносит удар {self.weapon.attack()}")
        else:
            print(f"{self.name} безоружен!")

class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"Монстр {self.name}  побежден!")


fighter = Fighter("Боец")
monster = Monster("Дракон")

fighter.change_weapon(Sword())
fighter.attack()
monster.defeat()

fighter.change_weapon(Bow())
fighter.attack()
monster.defeat()



