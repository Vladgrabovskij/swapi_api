import swapi
def get_film_info(film_id):
    film = swapi.get_film(film_id)
    if not film:
        print("Фільм з вказаним ідентифікатором не знайдено.")
        return

    print(f"Фільм: {film.title}")

    print("Персонажі:")
    for character in film.characters:
        character_info = swapi.get_person(character.split('/')[-2])
        print(f" {character_info.name} з планети {swapi.get_planet(character_info.homeworld.split('/')[-2]).name}")

    print("Транспортні засоби:")
    for vehicle in film.vehicles:
        vehicle_info = swapi.get_vehicle(vehicle.split('/')[-2])
        print(f" {vehicle_info.name}")

    print("Космічні кораблі:")
    for starship in film.starships:
        starship_info = swapi.get_starship(starship.split('/')[-2])
        print(f" {starship_info.name}")

    print("Види істот:")
    for species in film.species:
        species_info = swapi.get_species(species.split('/')[-2])
        print(f" {species_info.name}")


if __name__ == "__main__":
    film_id = input("Введіть ідентифікатор фільму: ")
    get_film_info(int(film_id))
