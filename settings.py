import pygame

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

TRANSLATIONS = {
    "en": {
        "main_menu": {
            "title": "The Racer",
            "options": ["Single Race", "Championship", "Practice", "Time Attack", "Settings", "Exit"],
            "high_score": "Best Lap: {:.2f}s"
        },
        "settings": {
            "options": ["Resolution", "Fullscreen", "Controls", "Music Volume", "SFX Volume", "Language", "AI Difficulty", "Minimap", "Car Collisions", "Fuel Consumption", "Weather", "Theme", "Back"],
            "minimap": ["On", "Off"],
            "collisions": ["On", "Off"],
            "fuel": ["None", "Low", "Medium", "High"],
            "weather": ["Sunny", "Rain", "Fog", "Night"],
            "fullscreen": ["On", "Off"],
            "theme": ["Default", "Dark", "Light", "Retro"]
        },
        "controls": {
            "prompt": "Press key for {}...",
            "controls": ["Up", "Down", "Left", "Right", "Pit Stop", "DRS"]
        },
        "race_setup": {
            "title": "Race Setup",
            "track": "Track: {}",
            "opponents": "Opponents: {}",
            "laps": "Laps: {}",
            "car_type": "Car Type: {}",
            "tire_type": "Tire Type: {}",
            "start": "Start Race",
            "back": "Back"
        },
        "practice_setup": {
            "title": "Practice Setup",
            "track": "Track: {}",
            "duration": "Duration: {} min",
            "car_type": "Car Type: {}",
            "tire_type": "Tire Type: {}",
            "start": "Start Practice",
            "back": "Back"
        },
        "championship_setup": {
            "title": "Championship Setup",
            "opponents": "Opponents: {}",
            "laps": "Laps per Race: {}",
            "practice": "Practice: {}",
            "practice_duration": "Practice Duration: {} min",
            "qualifying": "Qualifying: {}",
            "qualifying_duration": "Qualifying Duration: {} min",
            "car_type": "Car Type: {}",
            "tire_type": "Tire Type: {}",
            "start": "Start Championship",
            "back": "Back",
            "on_off": ["Off", "On"]
        },
        "time_attack_setup": {
            "title": "Time Attack Setup",
            "track": "Track: {}",
            "car_type": "Car Type: {}",
            "tire_type": "Tire Type: {}",
            "start": "Start Time Attack",
            "back": "Back"
        }
    },
    "pl": {
        "main_menu": {
            "title": "The Racer",
            "options": ["Wyścig Pojedynczy", "Mistrzostwa", "Praktyka", "Time Attack", "Ustawienia", "Wyjście"],
            "high_score": "Najlepsze Okrążenie: {:.2f}s"
        },
        "settings": {
            "options": ["Rozdzielczość", "Pełny Ekran", "Sterowanie", "Głośność Muzyki", "Głośność Efektów", "Język", "Trudność AI", "Minimapa", "Kolizje Samochodów", "Zużycie Paliwa", "Pogoda", "Motyw", "Wróć"],
            "minimap": ["Wł.", "Wył."],
            "collisions": ["Wł.", "Wył."],
            "fuel": ["Brak", "Niskie", "Średnie", "Wysokie"],
            "weather": ["Słonecznie", "Deszcz", "Mgła", "Noc"],
            "fullscreen": ["Wł.", "Wył."],
            "theme": ["Domyślny", "Ciemny", "Jasny", "Retro"]
        },
        "controls": {
            "prompt": "Naciśnij klawisz dla {}...",
            "controls": ["Góra", "Dół", "Lewo", "Prawo", "Pit Stop", "DRS"]
        },
        "race_setup": {
            "title": "Ustawienia Wyścigu",
            "track": "Tor: {}",
            "opponents": "Przeciwnicy: {}",
            "laps": "Okrążenia: {}",
            "car_type": "Typ Samochodu: {}",
            "tire_type": "Typ Opon: {}",
            "start": "Rozpocznij Wyścig",
            "back": "Wróć"
        },
        "practice_setup": {
            "title": "Ustawienia Praktyki",
            "track": "Tor: {}",
            "duration": "Czas: {} min",
            "car_type": "Typ Samochodu: {}",
            "tire_type": "Typ Opon: {}",
            "start": "Rozpocznij Praktykę",
            "back": "Wróć"
        },
        "championship_setup": {
            "title": "Ustawienia Mistrzostw",
            "opponents": "Przeciwnicy: {}",
            "laps": "Okrążenia na Wyścig: {}",
            "practice": "Praktyka: {}",
            "practice_duration": "Czas Praktyki: {} min",
            "qualifying": "Kwalifikacje: {}",
            "qualifying_duration": "Czas Kwalifikacji: {} min",
            "car_type": "Typ Samochodu: {}",
            "tire_type": "Typ Opon: {}",
            "start": "Rozpocznij Mistrzostwa",
            "back": "Wróć",
            "on_off": ["Wył.", "Wł."]
        },
        "time_attack_setup": {
            "title": "Ustawienia Time Attack",
            "track": "Tor: {}",
            "car_type": "Typ Samochodu: {}",
            "tire_type": "Typ Opon: {}",
            "start": "Rozpocznij Time Attack",
            "back": "Wróć"
        }
    },
    "fr": {
        "main_menu": {
            "title": "The Racer",
            "options": ["Course Unique", "Championnat", "Entraînement", "Contre-la-Montre", "Paramètres", "Quitter"],
            "high_score": "Meilleur Tour: {:.2f}s"
        },
        "settings": {
            "options": ["Résolution", "Plein Écran", "Commandes", "Volume Musique", "Volume Effets", "Langue", "Difficulté IA", "Minicarte", "Collisions Voitures", "Consommation Carburant", "Météo", "Thème", "Retour"],
            "minimap": ["Activé", "Désactivé"],
            "collisions": ["Activé", "Désactivé"],
            "fuel": ["Aucun", "Faible", "Moyen", "Élevé"],
            "weather": ["Ensoleillé", "Pluie", "Brouillard", "Nuit"],
            "fullscreen": ["Activé", "Désactivé"],
            "theme": ["Défaut", "Sombre", "Clair", "Rétro"]
        },
        "controls": {
            "prompt": "Appuyez sur une touche pour {}...",
            "controls": ["Haut", "Bas", "Gauche", "Droite", "Arrêt au Stand", "DRS"]
        },
        "race_setup": {
            "title": "Configuration de la Course",
            "track": "Circuit: {}",
            "opponents": "Adversaires: {}",
            "laps": "Tours: {}",
            "car_type": "Type de Voiture: {}",
            "tire_type": "Type de Pneus: {}",
            "start": "Démarrer la Course",
            "back": "Retour"
        },
        "practice_setup": {
            "title": "Configuration Entraînement",
            "track": "Circuit: {}",
            "duration": "Durée: {} min",
            "car_type": "Type de Voiture: {}",
            "tire_type": "Type de Pneus: {}",
            "start": "Démarrer Entraînement",
            "back": "Retour"
        },
        "championship_setup": {
            "title": "Configuration Championnat",
            "opponents": "Adversaires: {}",
            "laps": "Tours par Course: {}",
            "practice": "Entraînement: {}",
            "practice_duration": "Durée Entraînement: {} min",
            "qualifying": "Qualifications: {}",
            "qualifying_duration": "Durée Qualifications: {} min",
            "car_type": "Type de Voiture: {}",
            "tire_type": "Type de Pneus: {}",
            "start": "Démarrer Championnat",
            "back": "Retour",
            "on_off": ["Désactivé", "Activé"]
        },
        "time_attack_setup": {
            "title": "Configuration Contre-la-Montre",
            "track": "Circuit: {}",
            "car_type": "Type de Voiture: {}",
            "tire_type": "Type de Pneus: {}",
            "start": "Démarrer Contre-la-Montre",
            "back": "Retour"
        }
    },
    "de": {
        "main_menu": {
            "title": "The Racer",
            "options": ["Einzelrennen", "Meisterschaft", "Training", "Zeitfahren", "Einstellungen", "Beenden"],
            "high_score": "Beste Runde: {:.2f}s"
        },
        "settings": {
            "options": ["Auflösung", "Vollbild", "Steuerung", "Musiklautstärke", "Effektlautstärke", "Sprache", "KI-Schwierigkeit", "Minikarte", "Autokollisionen", "Kraftstoffverbrauch", "Wetter", "Thema", "Zurück"],
            "minimap": ["Ein", "Aus"],
            "collisions": ["Ein", "Aus"],
            "fuel": ["Kein", "Niedrig", "Mittel", "Hoch"],
            "weather": ["Sonnig", "Regen", "Nebel", "Nacht"],
            "fullscreen": ["Ein", "Aus"],
            "theme": ["Standard", "Dunkel", "Hell", "Retro"]
        },
        "controls": {
            "prompt": "Drücke Taste für {}...",
            "controls": ["Hoch", "Runter", "Links", "Rechts", "Boxenstopp", "DRS"]
        },
        "race_setup": {
            "title": "Renneinstellungen",
            "track": "Strecke: {}",
            "opponents": "Gegner: {}",
            "laps": "Runden: {}",
            "car_type": "Fahrzeugtyp: {}",
            "tire_type": "Reifentyp: {}",
            "start": "Rennen starten",
            "back": "Zurück"
        },
        "practice_setup": {
            "title": "Trainingseinstellungen",
            "track": "Strecke: {}",
            "duration": "Dauer: {} min",
            "car_type": "Fahrzeugtyp: {}",
            "tire_type": "Reifentyp: {}",
            "start": "Training starten",
            "back": "Zurück"
        },
        "championship_setup": {
            "title": "Meisterschaftseinstellungen",
            "opponents": "Gegner: {}",
            "laps": "Runden pro Rennen: {}",
            "practice": "Training: {}",
            "practice_duration": "Trainingsdauer: {} min",
            "qualifying": "Qualifikation: {}",
            "qualifying_duration": "Qualifikationsdauer: {} min",
            "car_type": "Fahrzeugtyp: {}",
            "tire_type": "Reifentyp: {}",
            "start": "Meisterschaft starten",
            "back": "Zurück",
            "on_off": ["Aus", "Ein"]
        },
        "time_attack_setup": {
            "title": "Zeitfahren-Einstellungen",
            "track": "Strecke: {}",
            "car_type": "Fahrzeugtyp: {}",
            "tire_type": "Reifentyp: {}",
            "start": "Zeitfahren starten",
            "back": "Zurück"
        }
    }
}
