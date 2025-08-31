import pygame
from pygame.math import Vector2

class Track:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.checkpoints = []
        self.start_positions = []
        self.pit_lane = []
        self.drs_zones = []
        self.walls = []
        self.finish_line = None
        self.define_track()

    def define_track(self):
        # Ultra-wide track for easy drivability
        if self.name == "Monaco":
            self.checkpoints = [
                pygame.Rect(250, 750, 300, 300),  # Start/finish
                pygame.Rect(750, 750, 300, 300),  # Bottom right
                pygame.Rect(750, 250, 300, 300),  # Mid right
                pygame.Rect(750, 50, 300, 300),   # Top right
                pygame.Rect(250, 50, 300, 300),   # Top left
                pygame.Rect(50, 50, 300, 300),    # Top left corner
                pygame.Rect(50, 250, 300, 300),   # Mid left
                pygame.Rect(50, 750, 300, 300),   # Bottom left
            ]
            self.start_positions = [(400, 850)]
            self.pit_lane = [pygame.Rect(250, 900, 500, 50)]
            self.drs_zones = [pygame.Rect(650, 750, 300, 50)]
            self.walls = [
                pygame.Rect(30, 30, 20, 940),    # Left outer wall
                pygame.Rect(950, 30, 20, 940),   # Right outer wall
                pygame.Rect(30, 30, 940, 20),    # Top outer wall
                pygame.Rect(30, 950, 940, 20),   # Bottom outer wall
                pygame.Rect(150, 150, 20, 700),  # Left inner wall
                pygame.Rect(830, 150, 20, 700),  # Right inner wall
                pygame.Rect(150, 150, 700, 20),  # Top inner wall
                pygame.Rect(150, 830, 700, 20),  # Bottom inner wall
            ]
            self.finish_line = pygame.Rect(250, 750, 300, 20)
        else:  # Simplified default track
            self.checkpoints = [
                pygame.Rect(250, 750, 300, 300),
                pygame.Rect(750, 750, 300, 300),
                pygame.Rect(750, 250, 300, 300),
                pygame.Rect(750, 50, 300, 300),
                pygame.Rect(250, 50, 300, 300),
                pygame.Rect(50, 50, 300, 300),
                pygame.Rect(50, 250, 300, 300),
                pygame.Rect(50, 750, 300, 300),
            ]
            self.start_positions = [(400, 850)]
            self.pit_lane = [pygame.Rect(250, 900, 500, 50)]
            self.drs_zones = [pygame.Rect(650, 750, 300, 50)]
            self.walls = [
                pygame.Rect(30, 30, 20, 940),
                pygame.Rect(950, 30, 20, 940),
                pygame.Rect(30, 30, 940, 20),
                pygame.Rect(30, 950, 940, 20),
                pygame.Rect(150, 150, 20, 700),
                pygame.Rect(830, 150, 20, 700),
                pygame.Rect(150, 150, 700, 20),
                pygame.Rect(150, 830, 700, 20),
            ]
            self.finish_line = pygame.Rect(250, 750, 300, 20)

    def draw(self, surface, scale=1.0):
        track_surface = pygame.Surface((self.width * scale, self.height * scale))
        track_surface.fill((100, 100, 100))  # Gray track
        for wall in self.walls:
            scaled_wall = pygame.Rect(wall.x * scale, wall.y * scale, wall.width * scale, wall.height * scale)
            pygame.draw.rect(track_surface, (50, 50, 50), scaled_wall)  # Dark gray walls
        for cp in self.checkpoints:
            scaled_cp = pygame.Rect(cp.x * scale, cp.y * scale, cp.width * scale, cp.height * scale)
            pygame.draw.rect(track_surface, (0, 255, 0, 100), scaled_cp, 1)  # Green checkpoints
        for drs in self.drs_zones:
            scaled_drs = pygame.Rect(drs.x * scale, drs.y * scale, drs.width * scale, drs.height * scale)
            pygame.draw.rect(track_surface, (0, 0, 255, 100), scaled_drs)  # Blue DRS zones
        for pit in self.pit_lane:
            scaled_pit = pygame.Rect(pit.x * scale, pit.y * scale, pit.width * scale, pit.height * scale)
            pygame.draw.rect(track_surface, (200, 200, 200), scaled_pit)  # Light gray pit lane
        if self.finish_line:
            scaled_finish = pygame.Rect(self.finish_line.x * scale, self.finish_line.y * scale, self.finish_line.width * scale, self.finish_line.height * scale)
            pygame.draw.rect(track_surface, (255, 255, 255), scaled_finish)  # White finish line
            for i in range(int(scaled_finish.width / (10 * scale))):
                color = (0, 0, 0) if i % 2 == 0 else (255, 255, 255)
                pygame.draw.rect(track_surface, color, (scaled_finish.x + i * 10 * scale, scaled_finish.y, 10 * scale, scaled_finish.height))
        surface.blit(track_surface, (0, 0))

    def check_collision(self, rect):
        for wall in self.walls:
            if rect.colliderect(wall):
                return True
        return False

    def check_checkpoint(self, rect, car):
        if car.checkpoint < len(self.checkpoints) and rect.colliderect(self.checkpoints[car.checkpoint]):
            return True
        return False

    def check_pitstop(self, rect):
        for pit in self.pit_lane:
            if rect.colliderect(pit):
                return True
        return False

    def check_drs_zone(self, rect):
        for drs in self.drs_zones:
            if rect.colliderect(drs):
                return True
        return False
