size = 400
pos = [size/2,size/2]
vel = [0,0]
accel = [0,0]

Kdx = 0.0001
Kix = 0.00001
Kpx = 0.001
dt = 0.001

integralx = 0 
errorx = 0
errorx_last = 0

Kdy = 0.0001
Kiy = 0.00001
Kpy = 0.001

integraly = 0 
errory = 0
errory_last = 0

chaser = [0,0]
chaserv = [0,0]
chasera = [0,0]

function setup() {
  createCanvas(size, size);
}

function draw() {
  background(20);

  translate(width / 2 - chaser[0], height / 2 - chaser[1]);
//  translate(width / 2 - pos[0], height / 2 - pos[1]);  
  errorx_last = errorx
  errory_last = errory
  errorx = pos[0] - chaser[0]
  errory = pos[1] - chaser[1]
  
a = floor(random(0,4))
print(((pos[0]-chaser[0])**2 + (pos[1]-chaser[1])**2)**(1/2))
  print(chaser[0]-pos[0])
  if(a == 1){
    accel[0] += 0.1
  }
  if(a == 0){
    accel[0] -= 0.1
  }
  if(a == 3){
    accel[1] += 0.1
  }
  if(a == 2){
    accel[1] -= 0.1
  }
  for(i = 0;i<2;i++){
    pos[i] += accel[i]
    vel[i] += accel[i]
    chaserv[i] += chasera[i]
    chaser[i] += chaserv[i]
  }

  integralx += errorx * dt
  integraly += errory * dt
  
  chasera[0] = Kix * integralx + Kpx * errorx + Kdx * (errorx - errorx_last)/dt
  chasera[1] = Kiy * integraly + Kpy * errory + Kdy * (errory - errory_last)/dt
  fill('blue')
  circle(pos[0],pos[1],10)
  fill('red')
  circle(chaser[0],chaser[1],10)
}