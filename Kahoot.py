```python
from javascript import require
import sys
from ultraviolet import Sidebar, GameCard, Theme, Particle

Kahoot = require("kahoot.js-latest")
import platform

def join_kahoot(game_pin: str, nickname: str):
    print(f"Joining Kahoot game {game_pin} with the nickname {nickname}")
    Kahoot.join(game_pin, nickname)


def flood_bots(game_pin: str, nickname: str, num_bots: int):
    print("Creating bot accounts...")
    for i in range(num_bots):
        join_kahoot(game_pin, f"{nickname} {i + 1}")
    print("Done creating bots.")


def main():
    version = platform.python_version()
    if version[0] != '3':
        print("This script requires Python 3 to run. Please update your Python version.")
        sys.exit()

    # Create a sidebar and a game card
    sidebar = Sidebar(title="Kahoot Bot", description="Flood a Kahoot game with bots.")
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

    # Add the game card to the sidebar
    sidebar.add_card(game_card)

    # Get the game_pin, nickname, and num_bots from the user
    sidebar.add_input("text", "game_pin", "Game PIN:", "Enter the game PIN:")
    sidebar.add_input("text", "nickname", "Nickname:", "Enter your nickname:")
    sidebar.add_input("number", "num_bots", "Number of bots:", "Enter the number of bots you want to join the game with:")
    sidebar.add_button("Join Kahoot", "join_kahoot")

    # Define the event handler for the "Join Kahoot" button
    def join_kahoot(event: Event):
        game_pin = sidebar.get_input_value("game_pin")
        nickname = sidebar.get_input_value("nickname")
        num_bots = sidebar.get_input_value("num_bots")
        flood_bots(game_pin, nickname, num_bots)

    sidebar.on("click", "#join_kahoot", join_kahoot)

    # Render the sidebar
    sidebar.render()

    try:
        while True:
            pass  # Keep the script running, ensuring the bots stay in-game
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, exiting...")
        print("Please note that it may take a while for the bots to leave, so please be patient.")


if __name__ == "__main__":
    main()
```