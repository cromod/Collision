import numpy.random as rd
import numpy as np
from display import *
from solver import *

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
    
if __name__ == "__main__":
  ballList = initList(15)
  #ballList = [Ball(1., 10., np.array([20.,20.]), np.array([5.,5.])), Ball(1., 10., np.array([380.,380.]), np.array([-5.,-5.])),\
  #            Ball(1., 10., np.array([380.,20.]), np.array([-2.,2.])),Ball(1., 10., np.array([20.,380.]), np.array([2.,-2.]))]
  #ballList = triangleList()
  #ballList.append(solver.Ball(10., 10., np.array([111.,100.]) , np.array([40.,40.])))
  #ballList.append(solver.Ball(10., 10., np.array([380.,380.]) , np.array([-20.,-40.])))
  wlength = 400.
  step = 0.025
  run(ballList, step, wlength)
  
        
  