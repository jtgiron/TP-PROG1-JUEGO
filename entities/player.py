import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self.load_animations()
        self.current_animation = 'idle'
        self.frame_index = 0
        self.aniamtion_speed = 0.15

        self.image = self.animations[self.current_animation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        # Físicas
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_force = -15
        self.gravity = 0.8
        self.on_ground = False
        self.facing_right = True
        
    def load_animations(self):
        # Cargar imagenes para las animaciones
        animations =  {}
        base_path = os.path.join("assets", "player")
        for anim_name in os.listdir(base_path):
            folder = os.path.join(base_path, anim_name)
            if os.path.isdir(folder):
                frames = []
                for  filename in sorted(os.listdir(folder)):
                    img_path = os.path.join(folder, filename)
                    image = pygame.image.load(img_path).convert_alpha()
                    frames.append(image)
                animations[anim_name] = frames
        return animations


    def update(self, keys):
        self.handle_input(keys)
        self.apply_gravity()
        self.animate()  
        # Movimiento horizontal
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def handle_input(self, keys):
        self.vel_x = 0
        if keys[pygame.K_a]:
            self.vel_x = -self.speed
            self.current_animation = 'run'
            self.facing_right = False
        elif keys[pygame.K_d]:
            self.vel_x = self.speed
            self.current_animation = 'run'
            self.facing_right = True
        else:
            self.current_animation = 'idle'

        
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False
            self.current_animation = 'jump'

    def apply_gravity(self):
        self.vel_y += self.gravity
        if self.vel_y > 15:  # límite de caída
            self.vel_y = 15

    def animate(self):
        frames = self.animations[self.current_animation]
        self.frame_index += self.aniamtion_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0
        image = frames[int(self.frame_index)]

        if not self.facing_right:
            image = pygame.transform.flip(image, True, False)

        self.image = image
