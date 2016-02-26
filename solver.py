import numpy as np

class Ball:

  def __init__(self, mass, radius, position, velocity):
    self._mass = mass
    self._radius = radius
    self._position = position
    self._velocity = velocity
    self._vafter = np.copy(velocity)

  def computeStep(self, step, wlength):
    self._position += step * self._velocity
    
  def newVelocity(self):
    self._velocity = self._vafter
    
  def computeEnergy(ballList):
    return ball._mass*np.linalg.norm(ball._velocity)**2
  
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

def solveStep(ballList, step, wlength):
  ballList = step1(ballList, step, wlength)
  ballList = step2(ballList, step, wlength)
  return ballList

def step1(ballList, step, wlength):
  indexList = range(len(ballList))
  for i in indexList:
    ballList[i].computeRefl(step,wlength)
    for j in indexList:
      if i!=j:
        ballList[i].computeColl(ballList[j],step,wlength)  
  return ballList

def step2(ballList, step, wlength):
  indexList = range(len(ballList)) 
  for i in indexList:
    ballList[i].newVelocity()
    ballList[i].computeStep(step,wlength)
  return ballList

