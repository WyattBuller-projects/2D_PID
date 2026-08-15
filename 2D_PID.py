import matplotlib.pyplot as plt
import numpy as np

#import pygame

size = 1000
steps = 4000

dt = 0.001
n_runs = 10
results = []
Kp = np.logspace(1,5,n_runs)
Ki = np.logspace(-4,1,n_runs)
Ki[-1] = (0)
Kd = np.logspace(0,2,n_runs)

def PID_SIM(Kp,Ki,Kd):
    chaser_pos = np.zeros(2,float)
    chaser_vel = np.zeros(2,float)
    chaser_accel = np.zeros(2,float)
    max_accel = 500.0
    pos = np.array([200.0,200.0])
    error = pos - chaser_pos
    error_history = np.zeros((steps,2),float)
    integral = np.zeros(2,float)
    
    error_last = pos - chaser_pos
    vel = np.zeros(2,float)
    for i in range(steps):
        a = np.random.randint(0,4)
        if a == 0:
            vel[0] += 1000.0 * dt
        elif a == 1:
            vel[0] -= 1000.0 * dt
        elif a == 2:
            vel[1] += 1000.0 * dt
        elif a == 3:
            vel[1] -= 1000.0 * dt
        
        error_last = error.copy()
        error =  pos - chaser_pos
        if np.linalg.norm(chaser_accel) < max_accel:
             integral += error * dt

        chaser_accel = Ki * integral + Kp * error + Kd * (error - error_last)/dt
        chaser_accel = np.clip(chaser_accel, -max_accel, max_accel)
        chaser_vel += chaser_accel * dt
        chaser_pos += chaser_vel * dt
        pos += vel * dt
        error_history[i] = error.copy()
    return error_history
for i in Kp:
    for j in Ki:
        for k in Kd: 
            gromp = PID_SIM(i,j,k)
            results.append({
                "Kp": i,
                "Ki": j,
                "Kd": k,
                "error": gromp,
                "error_magnitude": np.linalg.norm(gromp, axis=1)
                })
IST = np.zeros(len(results))
for i in range(len(results)):
    for j in range(int(steps/10),steps):
        IST[i] += results[i]["error_magnitude"][j]**2 * dt
print(f'Max IST is {np.max(IST)}')
print(f'Min IST is {np.min(IST)}') 
top5 = np.argsort(IST)[:5]
worst = np.argmax(IST)
for i in top5:
    print(f'The {i} result is top 5 with Kp of {results[i]["Kp"]}, Ki of {results[i]["Ki"]}, and Kd of {results[i]["Kd"]}. its IST is {IST[i]}')
print(f'worst  Kp is {results[worst]["Kp"]}')
print(f'worst  Ki is {results[worst]["Ki"]}')
print(f'worst  Kd is {results[worst]["Kd"]}')
for i in top5:
    plt.plot(results[i]["error_magnitude"])
    print(f'The final error is {results[i]["error_magnitude"][-1]}')
#for i in range(len(results)):
#	plt.plot(results[i]["error_magnitude"])
plt.show()

#pygame.init()
#screen = pygame.display.set_mode((size, size)) 
#clock = pygame.time.Clock()

#running = True
#while running:

#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False



#    pygame.display.flip()
#    clock.tick(60)
   

#pygame.quit()