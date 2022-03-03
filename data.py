import requests

# Trivia API : https://opentdb.com/api_config.php

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
quiz_data = response.json()