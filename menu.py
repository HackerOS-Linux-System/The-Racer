import pygame
import math
from settings import TRANSLATIONS
from constants import RESOLUTIONS, DIFFICULTIES, LANGUAGES, FUEL_CONSUMPTIONS, WEATHERS, THEMES, TRACKS, CAR_TYPES, TIRE_TYPES, OPPONENTS, LAPS, DURATIONS

def load_logo():
    try:
        return pygame.image.load("assets/Game-Logo.png")
    except:
        surface = pygame.Surface((120, 60))
        surface.fill((255, 50, 50))
        return surface

logo = load_logo()

def draw_menu(screen, font, title, options, selected, settings, lang, extra_texts=None):
    hover_time = 0
    last_time = pygame.time.get_ticks()
    while True:
        current_time = pygame.time.get_ticks()
        dt = (current_time - last_time) / 1000.0
        last_time = current_time
        bg_color = (240, 240, 240) if settings.get("theme", "default") == "light" else (50, 50, 50) if settings["theme"] == "dark" else (100, 100, 100) if settings["theme"] == "retro" else (220, 220, 220)
        screen.fill(bg_color)
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 50))
        screen.blit(overlay, (0, 0))
        screen.blit(logo, (screen.get_width() - logo.get_width() - 20, 20))

        title_text = font.render(title, True, (0, 0, 255))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 80))

        if extra_texts:
            for text, pos in extra_texts:
                screen.blit(text, pos)

        for i, option in enumerate(options):
            color = (255, 50, 50) if i == selected else (255, 255, 255)
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(screen.get_width() // 2, 220 + i * 70))
            if i == selected:
                hover_time += dt
                scale = 1.1 + 0.05 * math.sin(hover_time * 3)
                text = pygame.transform.scale(text, (int(text.get_width() * scale), int(text.get_height() * scale)))
                text_rect = text.get_rect(center=text_rect.center)
                pygame.draw.rect(screen, (200, 200, 255, 200), text_rect.inflate(30, 15), border_radius=8)
            screen.blit(text, text_rect)

        pygame.display.flip()
        return hover_time, last_time

def main_menu(screen, font, settings, high_score):
    options = TRANSLATIONS[settings["language"]]["main_menu"]["options"]
    selected = 0
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        score_text = font.render(TRANSLATIONS[settings["language"]]["main_menu"]["high_score"].format(high_score), True, (0, 128, 0))
        extra_texts = [(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 140))]
        hover_time, last_time = draw_menu(screen, font, TRANSLATIONS[settings["language"]]["main_menu"]["title"], options, selected, settings, settings["language"], extra_texts)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return "race_setup", settings
                    elif selected == 1:
                        return "championship", settings
                    elif selected == 2:
                        return "practice", settings
                    elif selected == 3:
                        return "time_attack", settings
                    elif selected == 4:
                        return "settings", settings
                    elif selected == 5:
                        pygame.quit()
                        exit()
        pygame.time.Clock().tick(60)

def settings_menu(screen, font, settings):
    options = TRANSLATIONS[settings["language"]]["settings"]["options"]
    selected = 0
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        extra_texts = [
            (font.render(f"{settings['resolution'][0]}x{settings['resolution'][1]}" if not settings["fullscreen"] else "Fullscreen", True, (0, 128, 0)), (500, 120)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["fullscreen"][0 if settings['fullscreen'] else 1], True, (0, 128, 0)), (500, 190)),
            (font.render("Press Enter to edit", True, (0, 128, 0)), (500, 260)),
            (font.render(f"{int(settings['music_volume'] * 100)}%", True, (0, 128, 0)), (500, 330)),
            (font.render(f"{int(settings['sfx_volume'] * 100)}%", True, (0, 128, 0)), (500, 400)),
            (font.render(settings['language'].upper(), True, (0, 128, 0)), (500, 470)),
            (font.render(settings['ai_difficulty'].capitalize(), True, (0, 128, 0)), (500, 540)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["minimap"][0 if settings['minimap_enabled'] else 1], True, (0, 128, 0)), (500, 610)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["collisions"][0 if settings['car_collisions'] else 1], True, (0, 128, 0)), (500, 680)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["fuel"][FUEL_CONSUMPTIONS.index(settings['fuel_consumption'])], True, (0, 128, 0)), (500, 750)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["weather"][WEATHERS.index(settings['weather'])], True, (0, 128, 0)), (500, 820)),
            (font.render(TRANSLATIONS[settings["language"]]["settings"]["theme"][THEMES.index(settings.get('theme', 'default'))], True, (0, 128, 0)), (500, 890))
        ]
        hover_time, last_time = draw_menu(screen, font, "Settings", options, selected, settings, settings["language"], extra_texts)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_RETURN:
                    if selected == 0 and not settings["fullscreen"]:
                        idx = RESOLUTIONS.index(settings["resolution"]) if settings["resolution"] in RESOLUTIONS else 0
                        settings["resolution"] = RESOLUTIONS[(idx + 1) % len(RESOLUTIONS)]
                    elif selected == 1:
                        settings["fullscreen"] = not settings["fullscreen"]
                        if settings["fullscreen"]:
                            settings["resolution"] = pygame.display.get_desktop_sizes()[0]
                        else:
                            settings["resolution"] = [1280, 720]
                    elif selected == 2:
                        settings["controls"] = controls_menu(screen, font, settings["controls"], settings["language"], settings)
                    elif selected == 5:
                        idx = LANGUAGES.index(settings["language"])
                        settings["language"] = LANGUAGES[(idx + 1) % len(LANGUAGES)]
                    elif selected == 6:
                        idx = DIFFICULTIES.index(settings["ai_difficulty"])
                        settings["ai_difficulty"] = DIFFICULTIES[(idx + 1) % len(DIFFICULTIES)]
                    elif selected == 7:
                        settings["minimap_enabled"] = not settings["minimap_enabled"]
                    elif selected == 8:
                        settings["car_collisions"] = not settings["car_collisions"]
                    elif selected == 9:
                        idx = FUEL_CONSUMPTIONS.index(settings['fuel_consumption'])
                        settings["fuel_consumption"] = FUEL_CONSUMPTIONS[(idx + 1) % len(FUEL_CONSUMPTIONS)]
                    elif selected == 10:
                        idx = WEATHERS.index(settings['weather'])
                        settings["weather"] = WEATHERS[(idx + 1) % len(WEATHERS)]
                    elif selected == 11:
                        idx = THEMES.index(settings.get('theme', 'default'))
                        settings["theme"] = THEMES[(idx + 1) % len(THEMES)]
                    elif selected == 12:
                        return settings
                if event.key == pygame.K_LEFT:
                    if selected == 3:
                        settings["music_volume"] = max(settings["music_volume"] - 0.1, 0.0)
                    elif selected == 4:
                        settings["sfx_volume"] = max(settings["sfx_volume"] - 0.1, 0.0)
                if event.key == pygame.K_RIGHT:
                    if selected == 3:
                        settings["music_volume"] = min(settings["music_volume"] + 0.1, 1.0)
                    elif selected == 4:
                        settings["sfx_volume"] = min(settings["sfx_volume"] + 0.1, 1.0)
                if event.key == pygame.K_ESCAPE:
                    return settings
        pygame.time.Clock().tick(60)

def controls_menu(screen, font, controls, lang, settings):
    keys = ["up", "down", "left", "right", "pit_stop", "drs"]
    selected = 0
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        options = [f"{TRANSLATIONS[lang]['controls']['controls'][i]}: {pygame.key.name(controls.get(k, pygame.K_UNKNOWN))}" for i, k in enumerate(keys)]
        hover_time, last_time = draw_menu(screen, font, "Controls", options, selected, settings, lang)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(keys)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(keys)
                    hover_time = 0
                if event.key == pygame.K_RETURN:
                    editing = keys[selected]
                    edit_text = font.render(TRANSLATIONS[lang]["controls"]["prompt"].format(TRANSLATIONS[lang]["controls"]["controls"][selected]), True, (0, 0, 255))
                    screen.blit(edit_text, (150, screen.get_height() - 80))
                    pygame.display.flip()
                    waiting = True
                    while waiting:
                        for ev in pygame.event.get():
                            if ev.type == pygame.KEYDOWN:
                                controls[editing] = ev.key
                                waiting = False
                if event.key == pygame.K_ESCAPE:
                    return controls
        pygame.time.Clock().tick(60)

def race_setup_menu(screen, font, settings):
    selected = 0
    track_idx = 0
    opponent_idx = 0
    lap_idx = 1
    car_idx = 1
    tire_idx = 1
    lang = settings["language"]
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        options = [
            TRANSLATIONS[lang]["race_setup"]["track"].format(TRACKS[track_idx]),
            TRANSLATIONS[lang]["race_setup"]["opponents"].format(OPPONENTS[opponent_idx]),
            TRANSLATIONS[lang]["race_setup"]["laps"].format(LAPS[lap_idx]),
            TRANSLATIONS[lang]["race_setup"]["car_type"].format(CAR_TYPES[car_idx]),
            TRANSLATIONS[lang]["race_setup"]["tire_type"].format(TIRE_TYPES[tire_idx]),
            TRANSLATIONS[lang]["race_setup"]["start"],
            TRANSLATIONS[lang]["race_setup"]["back"]
        ]
        hover_time, last_time = draw_menu(screen, font, TRANSLATIONS[lang]["race_setup"]["title"], options, selected, settings, lang)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        track_idx = (track_idx - 1) % len(TRACKS)
                    elif selected == 1:
                        opponent_idx = (opponent_idx - 1) % len(OPPONENTS)
                    elif selected == 2:
                        lap_idx = (lap_idx - 1) % len(LAPS)
                    elif selected == 3:
                        car_idx = (car_idx - 1) % len(CAR_TYPES)
                    elif selected == 4:
                        tire_idx = (tire_idx - 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RIGHT:
                    if selected == 0:
                        track_idx = (track_idx + 1) % len(TRACKS)
                    elif selected == 1:
                        opponent_idx = (opponent_idx + 1) % len(OPPONENTS)
                    elif selected == 2:
                        lap_idx = (lap_idx + 1) % len(LAPS)
                    elif selected == 3:
                        car_idx = (car_idx + 1) % len(CAR_TYPES)
                    elif selected == 4:
                        tire_idx = (tire_idx + 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RETURN:
                    if selected == 5:
                        return TRACKS[track_idx], OPPONENTS[opponent_idx], LAPS[lap_idx], CAR_TYPES[car_idx], TIRE_TYPES[tire_idx], settings
                    elif selected == 6:
                        return None, None, None, None, None, settings
                if event.key == pygame.K_ESCAPE:
                    return None, None, None, None, None, settings
        pygame.time.Clock().tick(60)

def practice_setup_menu(screen, font, settings):
    selected = 0
    track_idx = 0
    duration_idx = 1
    car_idx = 1
    tire_idx = 1
    lang = settings["language"]
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        options = [
            TRANSLATIONS[lang]["practice_setup"]["track"].format(TRACKS[track_idx]),
            TRANSLATIONS[lang]["practice_setup"]["duration"].format(DURATIONS[duration_idx]),
            TRANSLATIONS[lang]["practice_setup"]["car_type"].format(CAR_TYPES[car_idx]),
            TRANSLATIONS[lang]["practice_setup"]["tire_type"].format(TIRE_TYPES[tire_idx]),
            TRANSLATIONS[lang]["practice_setup"]["start"],
            TRANSLATIONS[lang]["practice_setup"]["back"]
        ]
        hover_time, last_time = draw_menu(screen, font, TRANSLATIONS[lang]["practice_setup"]["title"], options, selected, settings, lang)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        track_idx = (track_idx - 1) % len(TRACKS)
                    elif selected == 1:
                        duration_idx = (duration_idx - 1) % len(DURATIONS)
                    elif selected == 2:
                        car_idx = (car_idx - 1) % len(CAR_TYPES)
                    elif selected == 3:
                        tire_idx = (tire_idx - 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RIGHT:
                    if selected == 0:
                        track_idx = (track_idx + 1) % len(TRACKS)
                    elif selected == 1:
                        duration_idx = (duration_idx + 1) % len(DURATIONS)
                    elif selected == 2:
                        car_idx = (car_idx + 1) % len(CAR_TYPES)
                    elif selected == 3:
                        tire_idx = (tire_idx + 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RETURN:
                    if selected == 4:
                        return TRACKS[track_idx], DURATIONS[duration_idx], CAR_TYPES[car_idx], TIRE_TYPES[tire_idx], settings
                    elif selected == 5:
                        return None, None, None, None, settings
                if event.key == pygame.K_ESCAPE:
                    return None, None, None, None, settings
        pygame.time.Clock().tick(60)

def championship_setup_menu(screen, font, settings):
    selected = 0
    opponent_idx = 0
    lap_idx = 1
    practice_idx = 1
    practice_duration_idx = 1
    qualifying_idx = 1
    qualifying_duration_idx = 0
    car_idx = 1
    tire_idx = 1
    lang = settings["language"]
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        options = [
            TRANSLATIONS[lang]["championship_setup"]["opponents"].format(OPPONENTS[opponent_idx]),
            TRANSLATIONS[lang]["championship_setup"]["laps"].format(LAPS[lap_idx]),
            TRANSLATIONS[lang]["championship_setup"]["practice"].format(TRANSLATIONS[lang]["championship_setup"]["on_off"][practice_idx]),
            TRANSLATIONS[lang]["championship_setup"]["practice_duration"].format(DURATIONS[practice_duration_idx]),
            TRANSLATIONS[lang]["championship_setup"]["qualifying"].format(TRANSLATIONS[lang]["championship_setup"]["on_off"][qualifying_idx]),
            TRANSLATIONS[lang]["championship_setup"]["qualifying_duration"].format(DURATIONS[qualifying_duration_idx]),
            TRANSLATIONS[lang]["championship_setup"]["car_type"].format(CAR_TYPES[car_idx]),
            TRANSLATIONS[lang]["championship_setup"]["tire_type"].format(TIRE_TYPES[tire_idx]),
            TRANSLATIONS[lang]["championship_setup"]["start"],
            TRANSLATIONS[lang]["championship_setup"]["back"]
        ]
        hover_time, last_time = draw_menu(screen, font, TRANSLATIONS[lang]["championship_setup"]["title"], options, selected, settings, lang)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        opponent_idx = (opponent_idx - 1) % len(OPPONENTS)
                    elif selected == 1:
                        lap_idx = (lap_idx - 1) % len(LAPS)
                    elif selected == 2:
                        practice_idx = (practice_idx - 1) % 2
                    elif selected == 3:
                        practice_duration_idx = (practice_duration_idx - 1) % len(DURATIONS)
                    elif selected == 4:
                        qualifying_idx = (qualifying_idx - 1) % 2
                    elif selected == 5:
                        qualifying_duration_idx = (qualifying_duration_idx - 1) % len(DURATIONS)
                    elif selected == 6:
                        car_idx = (car_idx - 1) % len(CAR_TYPES)
                    elif selected == 7:
                        tire_idx = (tire_idx - 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RIGHT:
                    if selected == 0:
                        opponent_idx = (opponent_idx + 1) % len(OPPONENTS)
                    elif selected == 1:
                        lap_idx = (lap_idx + 1) % len(LAPS)
                    elif selected == 2:
                        practice_idx = (practice_idx + 1) % 2
                    elif selected == 3:
                        practice_duration_idx = (practice_duration_idx + 1) % len(DURATIONS)
                    elif selected == 4:
                        qualifying_idx = (qualifying_idx + 1) % 2
                    elif selected == 5:
                        qualifying_duration_idx = (qualifying_duration_idx + 1) % len(DURATIONS)
                    elif selected == 6:
                        car_idx = (car_idx + 1) % len(CAR_TYPES)
                    elif selected == 7:
                        tire_idx = (tire_idx + 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RETURN:
                    if selected == 8:
                        return (
                            OPPONENTS[opponent_idx],
                            LAPS[lap_idx],
                            bool(practice_idx),
                            DURATIONS[practice_duration_idx],
                            bool(qualifying_idx),
                            DURATIONS[qualifying_duration_idx],
                            CAR_TYPES[car_idx],
                            TIRE_TYPES[tire_idx],
                            settings
                        )
                    elif selected == 9:
                        return None, None, None, None, None, None, None, None, settings
                if event.key == pygame.K_ESCAPE:
                    return None, None, None, None, None, None, None, None, settings
        pygame.time.Clock().tick(60)

def time_attack_setup_menu(screen, font, settings):
    selected = 0
    track_idx = 0
    car_idx = 1
    tire_idx = 1
    lang = settings["language"]
    hover_time, last_time = 0, pygame.time.get_ticks()

    while True:
        options = [
            TRANSLATIONS[lang]["time_attack_setup"]["track"].format(TRACKS[track_idx]),
            TRANSLATIONS[lang]["time_attack_setup"]["car_type"].format(CAR_TYPES[car_idx]),
            TRANSLATIONS[lang]["time_attack_setup"]["tire_type"].format(TIRE_TYPES[tire_idx]),
            TRANSLATIONS[lang]["time_attack_setup"]["start"],
            TRANSLATIONS[lang]["time_attack_setup"]["back"]
        ]
        hover_time, last_time = draw_menu(screen, font, TRANSLATIONS[lang]["time_attack_setup"]["title"], options, selected, settings, lang)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                    hover_time = 0
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        track_idx = (track_idx - 1) % len(TRACKS)
                    elif selected == 1:
                        car_idx = (car_idx - 1) % len(CAR_TYPES)
                    elif selected == 2:
                        tire_idx = (tire_idx - 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RIGHT:
                    if selected == 0:
                        track_idx = (track_idx + 1) % len(TRACKS)
                    elif selected == 1:
                        car_idx = (car_idx + 1) % len(CAR_TYPES)
                    elif selected == 2:
                        tire_idx = (tire_idx + 1) % len(TIRE_TYPES)
                if event.key == pygame.K_RETURN:
                    if selected == 3:
                        return TRACKS[track_idx], CAR_TYPES[car_idx], TIRE_TYPES[tire_idx], settings
                    elif selected == 4:
                        return None, None, None, settings
                if event.key == pygame.K_ESCAPE:
                    return None, None, None, settings
        pygame.time.Clock().tick(60)
