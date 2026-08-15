import numpy as np
import pygame

size = 1000
steps = 1000

dt = 0.001
n_runs = 1

Kp = np.linspace(1e-4,1e-4,n_runs)
Ki = [0]
Kd = [0]
integral = np.zeros((n_runs,2))
error = np.zeros((n_runs,2))
error_last = np.zeros((n_runs,2))

chaser_pos = np.zeros((n_runs,2))
chaser_vel = np.zeros((n_runs,2))
chaser_accel = np.zeros((n_runs,2))
pos = np.array([200,200])
vel = np.zeros((n_runs,2))

def PID_SIM(Ki,Kp,Kd):
    


pygame.init()
screen = pygame.display.set_mode((size, size)) 
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()
    clock.tick(60)
   

pygame.quit()