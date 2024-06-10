class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    # GETTER / READER
    @property
    def pet_type(self):
        print("GETTING _pet_type")
        return self._pet_type

    # SETTER / WRITER
    @pet_type.setter
    def pet_type(self, new_pet_type):
        print("SETTING _pet_type")
        Hell = Exception
        if new_pet_type not in Pet.PET_TYPES:
            raise Hell(f"{new_pet_type} not in pet types")
        else:
            self._pet_type = new_pet_type


# parakeet.pet_type # activate the property GETTER
# parakeet.pet_type = "bird" # activate the pet_type SETTER


class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")

    def get_sorted_pets(self):
        # GET MY PETS
        my_pets = self.pets()
        # SORT MY PETS
        sorted_pets = sorted(my_pets, key=lambda each_pet: each_pet.name.lower())
        # RETURN EM
        return sorted_pets


# owner can have many pets
# pet belongs to owner

# Owner --< Pet

# FOCUS

# properties and setters

# making things private with the _ **

# syntax for methods and self

# isinstance
