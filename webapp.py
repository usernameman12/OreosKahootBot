```python
from flask import Flask, render_template, request, jsonify
from threading import Thread
from kahoot import flood_bots
import requests
import time

app = Flask(__name__)


def run_kahoot_bot(game_pin, nickname, num_bots):
    flood_bots(game_pin, nickname, num_bots)


def ping_self():
    while True:
      requests.get("https://rattle-icy-limit.glitch.me/")
      time.sleep(5)

# Sidebar links
sidebar_links = [
    {"name": "Home", "link": "/"},
    {"name": "Games", "link": "/games"},
    {"name": "Themes", "link": "/themes"},
    {"name": "Particles", "link": "/particles"},
]

# Game cards
game_cards = [
    {"name": "Kahoot!", "image": "/static/images/kahoot.png", "link": "/kahoot"},
    {"name": "Blooket", "image": "/static/images/blooket.png", "link": "/blooket"},
    {"name": "Quizizz", "image": "/static/images/quizizz.png", "link": "/quizizz"},
]

# Themes
themes = [
    {"name": "Light", "link": "/light"},
    {"name": "Dark", "link": "/dark"},
    {"name": "Blue", "link": "/blue"},
]

# Particles
particles = [
    {"name": "Snow", "link": "/snow"},
    {"name": "Rain", "link": "/rain"},
    {"name": "Fire", "link": "/fire"},
]

@app.route('/')
def index():
    return render_template('index.html', sidebar_links=sidebar_links, game_cards=game_cards, themes=themes, particles=particles)


@app.route('/start', methods=['POST'])
def start():
    game_pin = request.form['gamePin']
    nickname = request.form['nickname']
    amount = int(request.form['amount'])

    # Start the bot in a separate thread
    bot_thread = Thread(target=run_kahoot_bot, args=(game_pin, nickname, amount))
    bot_thread.start()

    return jsonify({'status': 'Bots are joining!'})


  
if __name__ == '__main__':
    ping_thread = Thread(target=ping_self)
    ping_thread.start()
    app.run(host='0.0.0.0', port=8080)
```