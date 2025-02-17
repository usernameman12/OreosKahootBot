```python
from flask import Flask, render_template, request, jsonify, redirect, url_for
from threading import Thread
from kahoot import flood_bots
import requests
import time
import ultraviolet
import random

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/game_site"
app.wsgi_app = ultraviolet.Middleware(app.wsgi_app)

# Client-side credentials are stored in ultraviolet.yml
# See https://github.com/titaniumnetwork-dev/Ultraviolet/wiki/Client-Side-Credentials

# Sidebar links
sidebar_links = [
    {"name": "Home", "link": "/"},
    {"name": "Games", "link": "/games"},
    {"name": "Themes", "link": "/themes"},
    {"name": "Particles", "link": "/particles"},
    {"name": "Settings", "link": "/settings"},
    {"name": "About", "link": "/about"},
    {"name": "Contact", "link": "/contact"},
]

# Game cards
game_cards = [
    {"name": "Kahoot!", "image": "/static/images/kahoot.png", "link": "/kahoot"},
    {"name": "Blooket", "image": "/static/images/blooket.png", "link": "/blooket"},
    {"name": "Quizizz", "image": "/static/images/quizizz.png", "link": "/quizizz"},
]

# Themes
themes = [
    {"name": "Light", "link": "/light", "css": "light.css"},
    {"name": "Dark", "link": "/dark", "css": "dark.css"},
    {"name": "Blue", "link": "/blue", "css": "blue.css"},
]

# Particles
particles = [
    {"name": "Snow", "link": "/snow", "js": "snow.js"},
    {"name": "Rain", "link": "/rain", "js": "rain.js"},
    {"name": "Fire", "link": "/fire", "js": "fire.js"},
]

@app.route('/')
def index():
    theme = random.choice(themes)["name"]
    particle = random.choice(particles)["name"]
    return render_template('index.html', sidebar_links=sidebar_links, game_cards=game_cards, themes=themes, particles=particles, theme=theme, particle=particle)


@app.route('/start', methods=['POST'])
def start():
    game_pin = request.form['gamePin']
    nickname = request.form['nickname']
    amount = int(request.form['amount'])

    # Start the bot in a separate thread
    bot_thread = Thread(target=flood_bots, args=(game_pin, nickname, amount))
    bot_thread.start()

    return jsonify({'status': 'Bots are joining!'})


@app.route('/about')
def about():
    return render_template('about.html', sidebar_links=sidebar_links)


@app.route('/contact')
def contact():
    return render_template('contact.html', sidebar_links=sidebar_links)


@app.route('/themes/<theme_name>')
def theme(theme_name):
    theme = next((theme for theme in themes if theme["name"] == theme_name), None)
    if not theme:
        return redirect(url_for('index'))

    return render_template('index.html', sidebar_links=sidebar_links, game_cards=game_cards, themes=themes, particles=particles, theme=theme["name"], particle=random.choice(particles)["name"], theme_css=theme["css"])


@app.route('/particles/<particle_name>')
def particle(particle_name):
    particle = next((particle for particle in particles if particle["name"] == particle_name), None)
    if not particle:
        return redirect(url_for('index'))

    return render_template('index.html', sidebar_links=sidebar_links, game_cards=game_cards, themes=themes, particles=particles, theme=random.choice(themes)["name"], particle=particle["name"], particle_js=particle["js"])


def ping_self():
    while True:
        try:
            requests.get("https://rattle-icy-limit.glitch.me/")
        except:
            pass
        time.sleep(5)


if __name__ == '__main__':
    ping_thread = Thread(target=ping_self)
    ping_thread.start()
    app.run(host='0.0.0.0', port=8080, debug=True)
```

Changes:

- Added debug=True to the app.run() call to enable debug mode. This will make it easier to debug any issues with the application.

- Fixed a typo in the start() route where the 'gamePin' form field was misspelled as 'gamepin'.

- Added a favicon.ico file to the static directory. This will display a favicon in the browser tab.

- Fixed a bug where the particle name was not being passed to the index.html template in the particle() route.

- Updated the kahoot.py module to use the latest version of the Kahoot! API.

- Added a README.md file to the project directory. This file provides instructions on how to run the application.

- Fixed a bug where the game cards were not displaying correctly on the index page.

- Added a robots.txt file to the project directory. This file tells search engines not to index the application.

- Updated the application to use the latest version of Flask.