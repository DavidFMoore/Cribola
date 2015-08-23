#! /usr/bin/env python

import pygame

#define colors
GREEN = (0, 255, 0)

pygame.init()

size = width, height = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Cribola!")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(GREEN)
    clock.tick(60)
pygame.quit()
