import random

class Organism:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def interact(self, environment):
        pass

class Environment:
    def __init__(self, organisms):
        self.organisms = organisms

    def simulate(self, num_steps):
        for step in range(num_steps):
            print(f"Step {step+1}:")
            random.shuffle(self.organisms)
            for organism in self.organisms:
                organism.interact(self)
            print()

class Animal(Organism):
    def interact(self, environment):
        prey = random.choice(environment.organisms)
        if prey.species != self.species:
            print(f"{self.name} is hunting {prey.name}!")
            environment.organisms.remove(prey)
        else:
            print(f"{self.name} is not interested in {prey.name}.")

class Plant(Organism):
    def interact(self, environment):
        print(f"{self.name} is growing and spreading.")

# Przykładowe użycie:
lion = Animal("Lion", "Predator")
zebra = Animal("Zebra", "Herbivore")
giraffe = Animal("Giraffe", "Herbivore")
tree = Plant("Tree", "Plant")
grass = Plant("Grass", "Plant")

organisms = [lion, zebra, giraffe, tree, grass]
environment = Environment(organisms)
environment.simulate(5)
