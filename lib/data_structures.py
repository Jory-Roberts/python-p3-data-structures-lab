import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    name_list = list()

    for food in spicy_foods :
        name_list.append(food["name"])

    return name_list


def get_spiciest_foods(spicy_foods):
    heat_level_list = []

    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_list.append(food)

    return heat_level_list


def print_spicy_foods(spicy_foods):
    emoji = '🌶'

    for food in spicy_foods :
        count = food['heat_level'] * emoji
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {count}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods :
        if food['cuisine'] == cuisine :
            return food


def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
