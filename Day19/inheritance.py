# print("class inheritance")
class Person:
    def move(self):
        print("move 4 paces")
    def rest(elf):
        print("Gains 4 health points ")
        
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")
class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("move 6 paces")
        
class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisible")
    def heal(self):
        print("Heals 15 health points")
        
character1 = Fighter()
character1.move()