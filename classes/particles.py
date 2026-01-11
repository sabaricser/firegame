import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, color, speed, duration):
        super().__init__()
        self.size = random.randint(2, 4)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.vel = pygame.Vector2(speed).rotate(random.uniform(0, 360))
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.start_time > self.duration:
            self.kill()
        
        # Fade out
        elapsed = now - self.start_time
        alpha = max(0, 255 - (elapsed / self.duration) * 255)
        self.image.set_alpha(alpha)
        
        self.rect.center += self.vel
        # Apply slight friction or gravity if needed
        self.vel *= 0.95

class ParticleSystem:
    def __init__(self):
        self.particles = pygame.sprite.Group()

    def create_burst(self, pos, color, count=10, speed_range=(1, 5), duration=500):
        for _ in range(count):
            speed = random.uniform(*speed_range)
            self.particles.add(Particle(pos, color, (speed, 0), duration))

    def update(self):
        self.particles.update()

    def draw(self, screen):
        self.particles.draw(screen)
