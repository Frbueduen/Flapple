# Flapple Bot: A Pokémon Discord Bot (Placeholder, Not Official)

## Overview

**Flapple Bot** is a feature-rich Pokémon Discord bot designed to bring the adventure of the Pokémon world directly to your server. Named after the Grass/Dragon-type Pokémon Flapple, this bot offers a variety of Pokémon-related functionalities—from catching wild Pokémon and choosing a starter, to managing your collection and exploring detailed Pokédex entries. Whether you're a casual trainer or a dedicated collector, Flapple Bot is your perfect companion for a true Pokémon journey.

## Features

### 🗂️ Pokémon Collection
- **Starter Selection:** Kick off your adventure with `%start` to choose your very own starter Pokémon.
- **Wild Encounters:** Encounter and catch wild Pokémon using the `%search` command.
- **Collection Management:** View your captured Pokémon with `%box` and get detailed info using `%view`.

### 📖 Pokédex & Moves
- **Pokédex:** Retrieve detailed information about any Pokémon using `%pokedex` (searchable by name or number).
- **Move Details:** Get comprehensive information about Pokémon moves via `%move`.

### 📈 Economy
- **In-Game Currency:** Earn Pokedollars as you catch Pokémon and complete your journey.
- **PokéMart:** Purchase items such as Pokéballs, Greatballs, and Ultraballs using `%pokemart`.
- **Balance Check:** Monitor your funds with the `%balance` command.

### 🔧 Utility
- **Partner Pokémon:** Check on your designated partner Pokémon using `%partner`.
- **Interactive Commands:** Enjoy a responsive bot with commands like `%ping` for quick latency checks.

### 🖼️ Data & Sprite Handling
- **Data Collection:** Pokémon data—including stats, evolution chains, and sprite URLs—is gathered using the `testing.py` script with data fetched from the PokeAPI.
- **Fallback Sprites:** The bot employs a robust sprite retrieval system in `get_best_sprite_url` to ensure a valid image is displayed, even when a primary URL returns a 404.

## Getting Started

1. **Invite Flapple Bot:**  
   Add the bot to your Discord server using the invite link provided in the repository.

2. **Set Up:**  
   Clone the repository, install dependencies, and configure your environment:
   ```bash
   git clone https://github.com/yourusername/flapple.git
   cd flapple
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Create a `.env` file in the root directory and add your Discord bot token:
   ```env
   API_Key=YOUR_DISCORD_BOT_TOKEN
   ```

3. **Fetch Pokémon Data (Optional):**  
   Run the data collection script to generate comprehensive Pokémon data:
   ```bash
   python testing.py
   ```
   This will create or update the JSON file containing Pokémon stats, evolution chains, and sprite URLs.

4. **Run the Bot:**  
   Start the bot by executing:
   ```bash
   python main.py
   ```

## Commands

### General
- **`%help`**: Display a list of commands and their descriptions.
- **`%ping`**: Check the bot's latency.

### Pokémon Management
- **`%start`**: Begin your adventure and choose your starter Pokémon.
- **`%search`**: Encounter and attempt to catch a wild Pokémon.
- **`%box`**: View your Pokémon collection in a paginated display.
- **`%view [number]`**: View detailed information about a specific Pokémon in your collection.
- **`%partner`**: Check details and level information of your partner Pokémon.

### Pokédex & Moves
- **`%pokedex [name or number]`**: Retrieve a detailed Pokédex entry for a Pokémon.
- **`%move [move name]`**: Get detailed information about a Pokémon move.

### Economy
- **`%balance`**: Check your current Pokedollar balance.
- **`%pokemart`**: Browse and purchase items from the in-game shop.

## Conclusion

Flapple Bot brings the excitement and adventure of the Pokémon world to your Discord server, offering a dynamic mix of catching wild Pokémon, managing your collection, and exploring detailed Pokédex entries. Whether you’re just starting your journey or already a seasoned trainer, Flapple Bot is designed to enhance your Pokémon experience. Invite Flapple Bot today and start your adventure!

---

For more information and support, visit the [Flapple Bot Support Server](#).