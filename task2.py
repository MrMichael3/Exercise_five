import random


### implement class Pokemon here ###
class Pokemon:
    def __init__(self, kind):
        self.__kind = kind
        self.__strength = random.randint(1, 255)
        self.__catchrate = random.randint(1, 10)

    def get_kind(self):
        return self.__kind

    def get_strength(self):
        return self.__strength

    def get_catchrate(self):
        return self.__catchrate

    def _reduce_strength(self, number):
        self.__strength -= number

    def attack(self, enemy):
        enemy._reduce_strength(1.1 * self.get_strength())

        ################################################################################


### implement class Trainer here ###
class Trainer:
    def __init__(self, name):
        self.__name = name
        self.__pokedex = []

    def get_name(self):
        return self.__name

    def get_pokemons(self):
        return self.__pokedex

    def catch_pokemon(self, pokemon):
        x = random.randint(1, 100)
        if x % int(Pokemon.get_catchrate(pokemon)) == 0:
            if len(self.__pokedex) < 6:
                print(self.__name + " has catched a " + pokemon.get_kind())
                self.__pokedex.append(pokemon)
            else:
                print(self.__name + " has already catched 6 pokemons.")
        else:
            print("The pokemon %s fled" % pokemon.get_kind())

    def print_pokemon_stats(self):
        if self.__pokedex == []:
            print("Trainer {0:s} has no pokemons".format(self.__name))
        index = 1  # intuitiver mit 1 anzufangen als mit 0
        for pokemon in self.__pokedex:
            print("Trainer {0}'s pokemon #{1} is a {2} with a strength of {3}".format(self.get_name(), index,
                                                                                      pokemon.get_kind(),
                                                                                      pokemon.get_strength()))
            index += 1

    def release_pokemon(self, index):
        if self.__pokedex[index] in self.__pokedex:
            self.__pokedex.pop(index)


################################################################################

def fight(trainer1, trainer2):
    "simulates a fight between to trainers and their pokemon"

    # get list of pokemon from both trainers
    pkmn_trainer1 = trainer1.get_pokemons()
    pkmn_trainer2 = trainer2.get_pokemons()

    # if both don't have any pokemon they cannot fight
    if pkmn_trainer1 == [] and pkmn_trainer2 == []:
        print("You cannot fight!")
        return

    # if only trainer2 has pokemon trainer2 wins
    elif pkmn_trainer1 == []:
        print("{0:s} has no pokemon left. {1:s} won!".format(trainer1.get_name(), trainer2.get_name()))
        return

    # if only trainer1 has pokemon trainer1 wins
    elif pkmn_trainer2 == []:
        print("{0:s} has no pokemon left. {1:s} won!".format(trainer2.get_name(), trainer1.get_name()))
        return

    # get the first pokemon they caught from both trainers
    active_pkmn_trainer1 = pkmn_trainer1[0]
    active_pkmn_trainer2 = pkmn_trainer2[0]

    # the two pokemon attack each other as long as none has below 0 strength
    # make sure only one pokemon attacks at a time
    start = bool(random.randint(0, 1))
    while active_pkmn_trainer1.get_strength() > 0 and active_pkmn_trainer2.get_strength() > 0:
        if start:
            active_pkmn_trainer1.attack(active_pkmn_trainer2)
            start = 0
        else:
            active_pkmn_trainer2.attack(active_pkmn_trainer1)
            start = 1

    # release the pokemon whose strength is below 0 (only consider the ones who just fought)
    if active_pkmn_trainer1.get_strength() <= 0:
        trainer1.release_pokemon(0)
    if active_pkmn_trainer2.get_strength() <= 0:
        trainer2.release_pokemon(0)
    # call next round of fighting recursively
    fight(trainer1, trainer2)


################################################################################

### test code ###

ash = Trainer("Ash")
ash.catch_pokemon(Pokemon("Pidgey"))
ash.catch_pokemon(Pokemon("Onix"))
ash.catch_pokemon(Pokemon("Azumarill"))
ash.catch_pokemon(Pokemon("Eevee"))
ash.catch_pokemon(Pokemon("Primeape"))
ash.catch_pokemon(Pokemon("Phanpy"))
ash.catch_pokemon(Pokemon("Rattata"))

misty = Trainer("Misty")
misty.catch_pokemon(Pokemon("Pidgey"))
misty.catch_pokemon(Pokemon("Onix"))
misty.catch_pokemon(Pokemon("Azumarill"))
misty.catch_pokemon(Pokemon("Eevee"))
misty.catch_pokemon(Pokemon("Primeape"))
misty.catch_pokemon(Pokemon("Phanpy"))
misty.catch_pokemon(Pokemon("Rattata"))

ash.print_pokemon_stats()
misty.print_pokemon_stats()

fight(ash, misty)
