import pygame
from car import Car, AICar
from track import Track
import time
import random
import menu

def pause_menu(screen, font, settings):
    options = ["Return to Menu", "Settings", "Exit Game"]
    translations = {
        "en": options,
        "pl": ["Wróć do Menu", "Ustawienia", "Wyjdź z Gry"],
        "fr": ["Retour au Menu", "Paramètres", "Quitter le Jeu"],
        "de": ["Zum Menü zurück", "Einstellungen", "Spiel beenden"]
    }
    lang = settings["language"]
    selected = 0
    while True:
        screen.fill((200, 200, 200, 150))
        for i, option in enumerate(translations[lang]):
            color = (255, 50, 50) if i == selected else (255, 255, 255)
            text = font.render(option, True, color)
            pygame.draw.rect(screen, (0, 0, 0, 200), text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + i * 60)).inflate(20, 10), border_radius=5)
            screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + i * 60)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return "menu"
                    elif selected == 1:
                        return "settings"
                    elif selected == 2:
                        return "exit"
                if event.key == pygame.K_ESCAPE:
                    return None

def race_mode(screen, track_name, num_opponents, max_laps, car_type, tire_type, settings, high_score):
    track = Track(track_name, 1280, 720)
    player = Car(track.start_positions[0][0], track.start_positions[0][1], car_type, tire_type)
    cars = [player]
    for i in range(num_opponents):
        x, y = track.start_positions[(i + 1) % len(track.start_positions)]
        cars.append(AICar(x, y, settings["ai_difficulty"], track, tire_type, name=f"AI_{i+1}"))
    font = pygame.font.SysFont("arial", 28, bold=True)
    clock = pygame.time.Clock()
    start_time = time.time()
    running = True
    race_finished = False
    standings = []
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return high_score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    action = pause_menu(screen, font, settings)
                    if action == "menu":
                        return high_score
                    elif action == "settings":
                        settings = menu.settings_menu(screen, font, settings)
                    elif action == "exit":
                        pygame.quit()
                        exit()
                if event.key == pygame.K_r and race_finished:
                    return high_score
        screen.fill((255, 255, 255) if settings["weather"] == "sunny" else (150, 150, 200) if settings["weather"] == "rain" else (100, 100, 150) if settings["weather"] == "fog" else (50, 50, 50))
        track.draw(screen)
        if not race_finished:
            for car in cars:
                car.update(keys if car == player else {}, settings["controls"], track, cars, settings["car_collisions"], settings["fuel_consumption"], settings["weather"])
                car.draw(screen)
        if settings["minimap_enabled"]:
            minimap_scale = 0.15
            minimap_surface = pygame.Surface((track.width * minimap_scale, track.height * minimap_scale))
            track.draw(minimap_surface, scale=minimap_scale)
            for car in cars:
                scaled_pos = (car.pos.x * minimap_scale, car.pos.y * minimap_scale)
                pygame.draw.circle(minimap_surface, car.color, scaled_pos, 4)
            screen.blit(minimap_surface, (screen.get_width() - minimap_surface.get_width() - 10, 10))
        hud_surface = pygame.Surface((220, 180), pygame.SRCALPHA)
        hud_surface.fill((0, 0, 0, 150))
        lap_text = font.render(f"Lap: {player.laps + 1}/{max_laps}" if max_laps else "Time Attack", True, (255, 255, 255))
        hud_surface.blit(lap_text, (10, 10))
        time_text = font.render(f"Time: {time.time() - start_time:.2f}s", True, (255, 255, 255))
        hud_surface.blit(time_text, (10, 40))
        fuel_text = font.render(f"Fuel: {player.fuel:.1f}%", True, (255, 255, 255))
        hud_surface.blit(fuel_text, (10, 70))
        tire_text = font.render(f"Tire: {player.tire_wear:.1f}%", True, (255, 255, 255))
        hud_surface.blit(tire_text, (10, 100))
        speed_text = font.render(f"Speed: {player.speed:.1f}", True, (255, 255, 255))
        hud_surface.blit(speed_text, (10, 130))
        drs_text = font.render("DRS Active" if player.drs_active else "DRS Off", True, (0, 255, 0) if player.drs_active else (255, 255, 255))
        hud_surface.blit(drs_text, (10, 160))
        screen.blit(hud_surface, (10, screen.get_height() - 190))
        if player.laps >= max_laps if max_laps is not None else False or player.fuel <= 0:
            if not race_finished:
                race_finished = True
                standings = sorted(cars, key=lambda x: (-x.laps, min(x.lap_times) if x.lap_times else float('inf')))
                if max_laps is None and player.lap_times:
                    new_high_score = min(player.lap_times)
                    high_score = min(high_score, new_high_score) if high_score > 0 else new_high_score
        if race_finished:
            result_surface = pygame.Surface((500, 400), pygame.SRCALPHA)
            result_surface.fill((0, 0, 0, 200))
            for i, car in enumerate(standings[:10]):
                standing_text = font.render(f"{i+1}. {car.name}: {min(car.lap_times):.2f}s" if car.lap_times else f"{i+1}. {car.name}: DNF", True, (255, 255, 255))
                result_surface.blit(standing_text, (250 - standing_text.get_width() // 2, 20 + i * 30))
            restart_text = font.render("Press R to Restart", True, (255, 50, 50))
            result_surface.blit(restart_text, (250 - restart_text.get_width() // 2, 350))
            screen.blit(result_surface, (screen.get_width() // 2 - 250, screen.get_height() // 2 - 200))
        pygame.display.flip()
        clock.tick(60)
    return high_score

def practice_mode(screen, track_name, duration, car_type, tire_type, settings):
    track = Track(track_name, 1280, 720)
    player = Car(track.start_positions[0][0], track.start_positions[0][1], car_type, tire_type)
    font = pygame.font.SysFont("arial", 28, bold=True)
    clock = pygame.time.Clock()
    start_time = time.time()
    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    action = pause_menu(screen, font, settings)
                    if action == "menu":
                        return
                    elif action == "settings":
                        settings = menu.settings_menu(screen, font, settings)
                    elif action == "exit":
                        pygame.quit()
                        exit()
                if event.key == pygame.K_r and time.time() - start_time > duration * 60:
                    return
        screen.fill((255, 255, 255) if settings["weather"] == "sunny" else (150, 150, 200) if settings["weather"] == "rain" else (100, 100, 150) if settings["weather"] == "fog" else (50, 50, 50))
        track.draw(screen)
        player.update(keys, settings["controls"], track, [player], settings["car_collisions"], settings["fuel_consumption"], settings["weather"])
        player.draw(screen)
        hud_surface = pygame.Surface((220, 180), pygame.SRCALPHA)
        hud_surface.fill((0, 0, 0, 150))
        time_text = font.render(f"Time Left: {max(0, duration * 60 - (time.time() - start_time)):.2f}s", True, (255, 255, 255))
        hud_surface.blit(time_text, (10, 10))
        fuel_text = font.render(f"Fuel: {player.fuel:.1f}%", True, (255, 255, 255))
        hud_surface.blit(fuel_text, (10, 40))
        tire_text = font.render(f"Tire: {player.tire_wear:.1f}%", True, (255, 255, 255))
        hud_surface.blit(tire_text, (10, 70))
        speed_text = font.render(f"Speed: {player.speed:.1f}", True, (255, 255, 255))
        hud_surface.blit(speed_text, (10, 100))
        drs_text = font.render("DRS Active" if player.drs_active else "DRS Off", True, (0, 255, 0) if player.drs_active else (255, 255, 255))
        hud_surface.blit(drs_text, (10, 130))
        screen.blit(hud_surface, (10, screen.get_height() - 150))
        if settings["minimap_enabled"]:
            minimap_scale = 0.15
            minimap_surface = pygame.Surface((track.width * minimap_scale, track.height * minimap_scale))
            track.draw(minimap_surface, scale=minimap_scale)
            scaled_pos = (player.pos.x * minimap_scale, player.pos.y * minimap_scale)
            pygame.draw.circle(minimap_surface, player.color, scaled_pos, 4)
            screen.blit(minimap_surface, (screen.get_width() - minimap_surface.get_width() - 10, 10))
        pygame.display.flip()
        clock.tick(60)
        if time.time() - start_time > duration * 60:
            return

def championship_mode(screen, font, settings, championship_standings):
    tracks = ["Monaco", "Silverstone", "Spa", "Monza", "Suzuka", "Interlagos", "Austin", "Abu Dhabi"]
    opponents, laps, practice_enabled, practice_duration, qualifying_enabled, qualifying_duration, car_type, tire_type, settings = menu.championship_setup_menu(screen, font, settings)
    if opponents is None:
        return None
    championship_standings = {f"AI_{i+1}": 0 for i in range(opponents)}
    championship_standings["Player"] = 0
    high_score = 0
    for track_name in tracks:
        if practice_enabled:
            practice_mode(screen, track_name, practice_duration, car_type, tire_type, settings)
        if qualifying_enabled:
            practice_mode(screen, track_name, qualifying_duration, car_type, tire_type, settings)
        high_score = race_mode(screen, track_name, opponents, laps, car_type, tire_type, settings, high_score)
        cars = [Car(0, 0, car_type, tire_type, name="Player")] + [AICar(0, 0, settings["ai_difficulty"], Track(track_name, 1280, 720), tire_type, name=f"AI_{i+1}") for i in range(opponents)]
        for car in cars:
            car.laps = random.randint(laps - 3, laps)
            car.lap_times = [random.uniform(45, 65) for _ in range(car.laps)] if car.laps > 0 else []
        standings = sorted(cars, key=lambda x: (-x.laps, min(x.lap_times) if x.lap_times else float('inf')))
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1] + [0] * (len(standings) - 10)
        for i, car in enumerate(standings):
            championship_standings[car.name] += points[min(i, len(points)-1)]
        screen.fill((255, 255, 255) if settings["weather"] == "sunny" else (150, 150, 200))
        result_font = pygame.font.SysFont("arial", 32, bold=True)
        for i, car in enumerate(standings[:10]):
            text = result_font.render(f"{i+1}. {car.name}: {min(car.lap_times):.2f}s" if car.lap_times else f"{i+1}. {car.name}: DNF", True, (255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0, 200), text.get_rect(center=(screen.get_width() // 2, 200 + i * 40)).inflate(20, 10), border_radius=5)
            screen.blit(text, text.get_rect(center=(screen.get_width() // 2, 200 + i * 40)))
        pygame.display.flip()
        pygame.time.wait(5000)
    screen.fill((255, 255, 255) if settings["weather"] == "sunny" else (150, 150, 200))
    sorted_standings = sorted(championship_standings.items(), key=lambda x: x[1], reverse=True)
    for i, (name, points) in enumerate(sorted_standings):
        text = result_font.render(f"{i+1}. {name}: {points} pts", True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0, 200), text.get_rect(center=(screen.get_width() // 2, 200 + i * 40)).inflate(20, 10), border_radius=5)
        screen.blit(text, text.get_rect(center=(screen.get_width() // 2, 200 + i * 40)))
    pygame.display.flip()
    pygame.time.wait(6000)
    return high_score, championship_standings
