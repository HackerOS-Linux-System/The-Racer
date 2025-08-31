import pygame
from pygame.math import Vector2

class Car:
    def __init__(self, x, y, car_type, tire_type):
        self.rect = pygame.Rect(x, y, 50, 25)  # Larger car for easier control
        self.speed = 0
        self.max_speed = 25 if car_type == "speed" else 20 if car_type == "balanced" else 15 if car_type == "accel" else 20
        self.acceleration = 1.5 if car_type == "accel" else 1.0  # Higher acceleration
        self.tire_grip = 2.0 if tire_type == "soft" else 1.6 if tire_type == "medium" else 1.2 if tire_type == "hard" else 1.4
        self.angle = 0
        self.checkpoint = 0
        self.lap = 1
        self.position = (x, y)

    def move(self, keys, controls, track, dt):
        # Gradual deceleration when no input
        if not keys[controls["up"]] and not keys[controls["down"]]:
            self.speed *= 0.9  # Softer deceleration

        # Accelerate forward
        if keys[controls["up"]]:
            self.speed = min(self.speed + self.acceleration * dt, self.max_speed)
            print(f"Accelerating: speed={self.speed:.2f}")  # Debug print
        # Decelerate or brake
        if keys[controls["down"]]:
            self.speed = max(self.speed - self.acceleration * dt, 0)
            print(f"Braking: speed={self.speed:.2f}")  # Debug print

        # Rotate (faster for responsiveness)
        if keys[controls["left"]]:
            self.angle += 1.2 * self.tire_grip * dt  # Increased rotation speed
        if keys[controls["right"]]:
            self.angle -= 1.2 * self.tire_grip * dt

        # Calculate movement
        direction = Vector2(0, -1).rotate_rad(self.angle)
        dx = self.speed * direction.x * dt
        dy = self.speed * direction.y * dt
        new_rect = self.rect.move(dx * 250, dy * 250)  # Higher movement scale

        # Check for collisions
        if not track.check_collision(new_rect):
            self.rect = new_rect
            self.position = (self.rect.x, self.rect.y)
        else:
            self.speed *= 0.95  # Minimal speed loss on collision
            self.rect.x -= dx * 150  # Stronger push-back
            self.rect.y -= dy * 150
            print(f"Collision detected: speed={self.speed:.2f}")  # Debug print

        # Check checkpoints
        if track.check_checkpoint(self.rect, self):
            self.checkpoint += 1
            print(f"Checkpoint {self.checkpoint} reached")  # Debug print
            if self.checkpoint >= len(track.checkpoints):
                self.checkpoint = 0
                self.lap += 1
                print(f"Lap {self.lap} completed")  # Debug print

    def draw(self, surface):
        # Rotate the car and add debug overlay
        car_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        car_surface.fill((255, 0, 0))  # Red car
        rotated_car = pygame.transform.rotate(car_surface, self.angle * 180 / 3.14159)
        rotated_rect = rotated_car.get_rect(center=self.rect.center)
        surface.blit(rotated_car, rotated_rect.topleft)
        # Debug: Draw hitbox and direction
        pygame.draw.rect(surface, (255, 255, 0, 100), self.rect, 1)  # Yellow hitbox
        direction = Vector2(0, -1).rotate_rad(self.angle) * 50
        pygame.draw.line(surface, (0, 255, 0), self.rect.center, (self.rect.centerx + direction.x, self.rect.centery + direction.y), 2)  # Green direction line
