import numpy as np
import numpy.random as rd
import Tkinter as tk
import time

class Error(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class Ball:

  def __init__(self, mass, radius, position, velocity):
    self._mass = mass
    self._radius = radius
    self._position = position
    self._velocity = velocity
    self._vafter = np.copy(velocity)

  def computeStep(self, step, wlength):
    self._position += step * self._velocity
    #less = np.less(self._position,np.zeros(2))
    #greater = np.greater(self._position,np.array([wlength,wlength]))
    #if less[0] or greater[0]:
      #self._position[0] %= wlength
    #if less[1] or greater[1]:
      #self._position[1] %= wlength  

  def computeColl(self, ball, step, wlength):
    m1 = self._mass
    m2 = ball._mass
    r1 = self._radius
    r2 = ball._radius
    v1 = self._velocity
    v2 = ball._velocity
    x1 = self._position
    x2 = ball._position
    di = x2-x1
    norm = np.linalg.norm(di)
    if norm-r1-r2 < step*abs(np.dot(v1-v2,di))/norm:
      self._vafter = v1 - 2.*m2/(m1+m2) * np.dot(v1-v2,di)/(np.linalg.norm(di)**2.) * di

  def computeRefl(self, step, wlength):
    r = self._radius
    v = self._velocity
    x = self._position
    projx = step*abs(np.dot(v,np.array([1.,0.])))
    projy = step*abs(np.dot(v,np.array([0.,1.])))
    if abs(x[0])-r < projx or abs(wlength-x[0])-r < projx:
      self._vafter[0] *= -1
    if abs(x[1])-r < projy or abs(wlength-x[1])-r < projy:
      self._vafter[1] *= -1.
      
  def newVelocity(self):
    self._velocity = self._vafter

def initList(N):
  ballList = []
  r = 10.
  v = 10.
  x = 400./float(N+1)
  for i in range(N):
    mrand = r*(1.-0.05*i)
    rrand = mrand
    vrand = v*np.array([-1.,1.])
    xrand = x*np.array([float(i+1),float(i+1)])
    ballList.append(Ball(mrand, rrand, xrand, vrand))
  return ballList

def triangleList():
  ballList = []
  r = 10.
  v = np.array([0.,0.])
  for i in range(3):
    for j in range(3):
      x = np.array([200.,200.])+30.*np.array([i,j])
      ballList.append(Ball(r, r, x, v))
  return ballList

def simulStep(ballList, step, wlength):
  #start = time.time()
  ballList = compute1(ballList, step, wlength)
  ballList = compute2(ballList, step, wlength)
  #end = time.time()
  #print end - start
  return ballList

def compute1(ballList, step, wlength):
  indexList = range(len(ballList))
  for i in indexList:
    ballList[i].computeRefl(step,wlength)
    for j in indexList:
      if i!=j:
        ballList[i].computeColl(ballList[j],step,wlength)  
  return ballList

def compute2(ballList, step, wlength):
  indexList = range(len(ballList)) 
  for i in indexList:
    ballList[i].newVelocity()
    ballList[i].computeStep(step,wlength)
  return ballList

def computeEnergy(ballList):
  return sum(ball._mass*np.linalg.norm(ball._velocity)**2 for ball in ballList)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _coords_circle(self, target, x, y, r, **kwargs):
    return self.coords(target, x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.coords_circle = _coords_circle

def draw(ballList,canvas):
  drawList = []
  for ball in ballList:
    position = ball._position.tolist()
    drawList.append(canvas.create_circle(position[0], position[1], ball._radius, fill="white"))
  return drawList

def move(ballList,drawList,canvas):
  for i in range(len(ballList)):
    position = ballList[i]._position.tolist()
    canvas.coords_circle(drawList[i],position[0], position[1],ballList[i]._radius)

def animation(ballList, wlength):
  flag = True
  while(flag):
    ballList=simulStep(ballList,0.025,wlength)
    move(ballList,drawList,canvas)
    canvas.update()
    #print computeEnergy(ballList)
    time.sleep(0.00001)
    
if __name__ == "__main__":
  #ballList = initList(15)
  #ballList = [Ball(1., 10., np.array([20.,20.]), np.array([5.,5.])), Ball(1., 10., np.array([380.,380.]), np.array([-5.,-5.])),\
  #            Ball(1., 10., np.array([380.,20.]), np.array([-2.,2.])),Ball(1., 10., np.array([20.,380.]), np.array([2.,-2.]))]
  ballList = triangleList()
  ballList.append(Ball(10., 10., np.array([161.,150.]) , np.array([40.,40.])))
  ballList.append(Ball(10., 10., np.array([350.,350.]) , np.array([-20.,-40.])))
  wlength = 400.
  window = tk.Tk()
  canvas = tk.Canvas(window, width=wlength, height=wlength, bg="black")
  canvas.pack()
  drawList=draw(ballList,canvas)
  canvas.pack()
  window.after(0,animation(ballList, wlength))
  window.mainloop()
        
  