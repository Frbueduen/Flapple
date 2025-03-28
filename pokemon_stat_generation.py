import json
import random
import os
from pymongo import MongoClient

def generate_iv():
    return random.randint(0, 31)

def calculate_stat(base, iv, level, ev=0, nature=1, is_hp=False):
    if is_hp:
        # HP formula: floor((2 * B + I + E) * L / 100 + L + 10)
        return int((2 * base + iv + (ev // 4)) * level // 100 + level + 10)
    else:
        # Other stats: floor(floor((2 * B + I + E) * L / 100 + 5) * N)
        return int((((2 * base + iv + (ev // 4)) * level) // 100 + 5) * nature)

def generate_unique_id():
    from main import unique_id_collection
    result = unique_id_collection.find_one_and_update(
        {},
        {"$inc": {"last_id": 1}},
        upsert=True,
        return_document=True
    )
    return str(result["last_id"]).zfill(6)

def generate_nature(partner_nature=None, has_synchronize=False):
    """
    Generate a Pokémon nature based on the following rules:
    - If partner has Synchronize ability, 50% chance to match partner's nature
    - Otherwise, randomly select from 25 available natures with equal probability
    
    :param partner_nature: The nature of the partner Pokémon (if applicable)
    :param has_synchronize: Whether the partner Pokémon has the Synchronize ability
    :return: The generated nature as a string
    """
    natures = [
        "Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty",
        "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky",
        "Rash", "Relaxed", "Sassy", "Serious", "Timid"
    ]
    
    # If partner has Synchronize and a valid nature, 50% chance to match
    if has_synchronize and partner_nature in natures:
        if random.random() < 0.5:
            return partner_nature
    
    # Otherwise, select a random nature with equal probability
    return random.choice(natures)


def store_caught_pokemon(pokemon_data, user_id, shiny, level, nature):
    from main import inventory_collection, pokemon_collection
    ivs = {
        "hp": generate_iv(),
        "attack": generate_iv(),
        "defense": generate_iv(),
        "special-attack": generate_iv(),
        "special-defense": generate_iv(),
        "speed": generate_iv()
    }

    unique_id = generate_unique_id()

    caught_pokemon = {
        "_id": unique_id,
        "pokedex_id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "nickname": None,
        "shiny": shiny,
        "level": level,
        "nature": nature,  
        "ivs": ivs,
        "base_stats": pokemon_data["stats"],
        "final_stats": {
            "hp": calculate_stat(pokemon_data["stats"]["hp"], ivs["hp"], level, is_hp=True),
            "attack": calculate_stat(pokemon_data["stats"]["attack"], ivs["attack"], level),
            "defense": calculate_stat(pokemon_data["stats"]["defense"], ivs["defense"], level),
            "special-attack": calculate_stat(pokemon_data["stats"]["special-attack"], ivs["special-attack"], level),
            "special-defense": calculate_stat(pokemon_data["stats"]["special-defense"], ivs["special-defense"], level),
            "speed": calculate_stat(pokemon_data["stats"]["speed"], ivs["speed"], level)
        },
        "xp": 0
    }

    # Insert the caught Pokémon data into MongoDB
    pokemon_collection.insert_one(caught_pokemon)

    # Update the user's inventory in MongoDB
    inventory_collection.update_one(
        {"_id": str(user_id)},
        {"$push": {"caught_pokemon": unique_id}},
        upsert=True
    )

    return unique_id