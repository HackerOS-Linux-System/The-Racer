import pygame
from track import Track
from car import Car

def run_race(screen, font, track_name, car_type, tire_type, num_laps, settings):
    clock = pygame.time.Clock()
    track = Track(track_name, 1000, 1000)  # Consistent track size
    car = Car(track.start_positions[0][0], track.start_positions[0][1], car_type, tire_type)
    running = True
    start_time = pygame.time.get_ticks()

    while running and car.lap <= num_laps:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        car.move(keys, settings["controls"], track, dt)

        screen.fill((0, 0, 0))
        track.draw(screen)
        car.draw(screen)
        lap_text = font.render(f"Lap: {car.lap}/{num_laps}", True, (255, 255, 255))
        speed_text = font.render(f"Speed: {car.speed:.2f}", True, (255, 255, 255))
        screen.blit(lap_text, (10, 10))
        screen.blit(speed_text, (10, 40))
        pygame.display.flip()

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
    print(f"Race finished in {elapsed_time:.2f} seconds")  # Debug print
    return elapsed_time
