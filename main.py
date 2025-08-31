import pygame
from menu import main_menu, race_setup_menu, championship_setup_menu, practice_setup_menu, time_attack_setup_menu, settings_menu
from game import run_race
from utils import load_game, save_game
from constants import DEFAULT_SETTINGS

def main():
    pygame.init()
    high_score, championship_standings, settings = load_game()
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode(settings["resolution"])
    pygame.display.set_caption("The Racer")

    while True:
        mode, settings = main_menu(screen, font, settings, high_score)
        if mode == "race_setup":
            track_name, num_opponents, num_laps, car_type, tire_type, settings = race_setup_menu(screen, font, settings)
            if track_name:
                elapsed_time = run_race(screen, font, track_name, car_type, tire_type, num_laps, settings)
                high_score = min(high_score, elapsed_time) if high_score else elapsed_time
                print(f"Race completed on {track_name} in {elapsed_time:.2f} seconds")
        elif mode == "championship":
            opponents, laps, practice, practice_duration, qualifying, qualifying_duration, car_type, tire_type, settings = championship_setup_menu(screen, font, settings)
            if opponents:
                print(f"Starting championship with {opponents} opponents, {laps} laps, practice: {practice}, qualifying: {qualifying}, car: {car_type}, tires: {tire_type}")
                # Placeholder for championship logic
        elif mode == "practice":
            track_name, duration, car_type, tire_type, settings = practice_setup_menu(screen, font, settings)
            if track_name:
                elapsed_time = run_race(screen, font, track_name, car_type, tire_type, 999, settings)
                print(f"Practice completed on {track_name} in {elapsed_time:.2f} seconds")
        elif mode == "time_attack":
            track_name, car_type, tire_type, settings = time_attack_setup_menu(screen, font, settings)
            if track_name:
                elapsed_time = run_race(screen, font, track_name, car_type, tire_type, 1, settings)
                high_score = min(high_score, elapsed_time) if high_score else elapsed_time
                print(f"Time attack completed on {track_name} in {elapsed_time:.2f} seconds")
        elif mode == "settings":
            settings = settings_menu(screen, font, settings)
            save_game(high_score, championship_standings, settings)
            pygame.display.set_mode(settings["resolution"], pygame.FULLSCREEN if settings["fullscreen"] else 0)
        else:
            save_game(high_score, championship_standings, settings)
            break

if __name__ == "__main__":
    main()
