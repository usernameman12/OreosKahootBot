```python
from javascript import require
import sys
from ultraviolet import Sidebar, GameCard, Theme, Particle

Kahoot = require("kahoot.js-latest")
import platform

def join_kahoot(game_pin: str, nickname: str):
    print(f"Creating client with name: {nickname}")
    Kahoot.join(game_pin, nickname)


def flood_bots(game_pin: str, nickname: str, num_bots: int):
    print("Flooding bots...")
    for i in range(num_bots):
        join_kahoot(game_pin, f"{nickname} {i + 1}")
    print("Done creating clients.")


def main():
    version = platform.python_version()
    if version[0] != '3':
        print("This script requires Python 3 to run. Please update your Python version.")
        sys.exit()

    # Create a sidebar and a game card
    sidebar = Sidebar()
    game_card = GameCard()

    # Add a custom theme to the game card
    theme = Theme()
    theme.primary_color = "skyblue"
    theme.secondary_color = "white"
    game_card.add_theme(theme)

    # Add a particle effect to the game card
    particle = Particle()
    particle.type = "snow"
    particle.color = "white"
    particle.size = 10
    game_card.add_particle(particle)

    # Set the title and description of the game card
    game_card.set_title("Kahoot Flooder")
    game_card.set_description("Flood a Kahoot game with bots.")

    # Add the game card to the sidebar
    sidebar.add_card(game_card)

    # Get the game_pin, nickname, and num_bots from the user
    game_pin = input("Game PIN: ")
    nickname = input("Nickname: ")
    num_bots = int(input("How many bots would you like to add?: "))
    print()
    try:
        flood_bots(game_pin, nickname, num_bots)
    except ValueError:
        print("Error joining kahoot, sorry...")
        sys.exit()

    try:
        while True:
            pass  # Keep the script running, ensuring the bots stay in-game
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, exiting...")
        print("Please note that it may take a while for the bots to leave, so please be patient.")


if __name__ == "__main__":
    main()
```