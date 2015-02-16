import pygame
from NameGenerator import *


class Unit(pygame.sprite.Sprite):
    dist = 32

    def __init__(self, team):
        pygame.sprite.Sprite.__init__(self)
        self.x = None
        self.y = None
        self.has_moved = False
        self.has_attacked = False
        self.team = team
        self.CurrentHealth = self.MaxHealth
        self.image = pygame.image.load(self.resource_path(self.img_src))
        self.rect = self.image.get_rect()
        self.attacking = False
        self.attack_start_frame = None
        self.name = NameGenerator.generate_name("Units/Names.txt")
        self.temp_movement = 0
        self.is_target = False
        self.damage = 0

    def draw(self, surface, animation_state, tapped):
        image_attributes = self.img_src.split("-")
        if not self.attacking:
            if tapped:
                image_attributes[2] = "1"
            else:
                image_attributes[2] = str(animation_state)

            self.image = pygame.image.load("-".join(image_attributes))
            if tapped:
                self.image.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            surface.blit(self.image, (self.x, self.y))
        else:
            image_attributes[1] = "Attack"
            if animation_state != self.attack_start_frame:
                attack_frame = 2
            else:
                attack_frame = 1

            image_attributes[2] = str(attack_frame)
            self.image = pygame.image.load("-".join(image_attributes))
            surface.blit(self.image, (self.x, self.y))

            if self.have_two_frames_passed(animation_state, self.attack_start_frame):
                    self.attacking = False
                    self.attack_start_frame = None

    def draw_preview(self, surface, location, animation_state, attacking):
        image_attributes = self.img_src.split("-")
        if not attacking:
            image_attributes[2] = str(animation_state)
            self.image = pygame.image.load("-".join(image_attributes))
        else:
            image_attributes[1] = "Attack"
            if animation_state % 2 == 0:
                attack_frame = 2
            else:
                attack_frame = 1

            image_attributes[2] = str(attack_frame)
            self.image = pygame.image.load("-".join(image_attributes))
            surface.blit(self.image, location)

        surface.blit(self.image, location)

    def incoming_damage(self, damage):
        self.damage = damage

    def selected_target(self):
        self.is_target = True

    def movement_clac(self):
        self.temp_movement -= 1

    def reset_movement(self):
        self.temp_movement = self.movement

    def get_location(self):
        current_space = (self.x / self.dist, self.y / self.dist)
        return current_space

    def get_team(self):
        return self.team

    def get_movement(self):
        return self.Movement

    def get_minimum_range(self):
        return self.MinimumRange

    def get_maximum_range(self):
        return self.MaximumRange

    def deal_damage(self, damage):
        self.CurrentHealth -= damage

    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )

    @staticmethod
    def have_two_frames_passed(first, current):
        return (current == 1 and first == 2) or (current == 2 and first == 3) or (current == 3 and first == 1)

