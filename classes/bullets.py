import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 10
        self.speed = 10
        # Add glow
        self.glow = pygame.Surface((self.image.get_width() + 10, self.image.get_height() + 10), pygame.SRCALPHA)
        pygame.draw.circle(self.glow, (100, 200, 255, 100), (self.glow.get_width()//2, self.glow.get_height()//2), self.glow.get_width()//2)
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    def update(self):
        self.rect.move_ip(0, -self.speed)

        if self.rect.top <= 1:
            self.kill()
