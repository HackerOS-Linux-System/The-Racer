import json
import os
import pygame
from settings import DEFAULT_SETTINGS

def load_game():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
            high_score = data.get("high_score", 0)
            championship_standings = data.get("championship_standings", {})
            settings = data.get("settings", DEFAULT_SETTINGS)
            for key, value in DEFAULT_SETTINGS.items():
                if key not in settings:
                    settings[key] = value
            return high_score, championship_standings, settings
    except:
        return 0, {}, DEFAULT_SETTINGS

def save_game(high_score, championship_standings, settings):
    data = {
        "high_score": high_score,
        "championship_standings": championship_standings,
        "settings": settings
    }
    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)
