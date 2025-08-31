import pygame

# Default game settings (moved from settings.py to avoid duplication)
DEFAULT_SETTINGS = {
    "resolution": [1280, 720],
    "fullscreen": False,
    "controls": {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "pit_stop": pygame.K_p,
        "drs": pygame.K_d
    },
    "music_volume": 0.0,
    "sfx_volume": 0.0,
    "language": "en",
    "ai_difficulty": "medium",
    "minimap_enabled": True,
    "car_collisions": True,
    "fuel_consumption": "medium",
    "weather": "sunny",
    "theme": "default"
}

# Game constants
RESOLUTIONS = [[800, 600], [1280, 720], [1920, 1080]]
DIFFICULTIES = ["easy", "medium", "hard"]
LANGUAGES = ["en", "pl", "fr", "de"]
FUEL_CONSUMPTIONS = ["none", "low", "medium", "high"]
WEATHERS = ["sunny", "rain", "fog", "night"]
THEMES = ["default", "dark", "light", "retro"]
TRACKS = ["Monaco", "Silverstone", "Spa"]
CAR_TYPES = ["speed", "balanced", "accel"]
TIRE_TYPES = ["soft", "medium", "hard"]
OPPONENTS = [0, 3, 7, 15]
LAPS = [1, 3, 5, 10]
DURATIONS = [5, 10, 15, 30]
