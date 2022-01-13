import imp
from multiprocessing.spawn import import_main_path
import pygame, sys

import random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (700, 512))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

pygame.init()
screen = pygame.display.set_mode((576, 1024))    #defining Display
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

# Surfaces
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Game Loop
while True:
    #check for closing of window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())


    # Bird
    screen.blit(bg_surface, (0,0))
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect )

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos == -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)
    