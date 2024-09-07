class breed:

    def __init__(self, breed, colour):

        self.breed = breed
        self.colour = colour

Dog1 = breed("Pomeranian", "White")
Dog2 = breed("German Shepherd", "Brown-Black")

print("Dog 1 Breed:", Dog1.breed)
print("Dog 1 colour:", Dog1.colour)

print("Dog 2 breed:", Dog2.breed)
print("Dog 2 colour:", Dog2.colour)
