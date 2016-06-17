import numpy.random as rd
import numpy as np
from display import *
from solver import *

def init_list(N):
    ball_list = []
    r = 10.
    v = 10.
    x = 400./float(N+1)
    for i in range(N):
        mrand = r*(1.-0.05*i)
        rrand = mrand
        vrand = v*np.array([-1.,1.])
        xrand = x*np.array([float(i+1),float(i+1)])
        ball_list.append(Ball(mrand, rrand, xrand, vrand))
    return ball_list

def triangle_list():
    ball_list = []
    r = 10.
    v = np.array([0.,0.])
    for i in range(3):
        for j in range(3):
            x = np.array([200.,200.])+30.*np.array([i,j])
            ball_list.append(Ball(r, r, x, v))
    return ball_list
        
if __name__ == "__main__":
    ball_list = init_list(10)
    #ball_list = [Ball(1., 10., np.array([20.,20.]), np.array([5.,5.])), Ball(1., 10., np.array([380.,380.]), np.array([-5.,-5.])),\
    #             Ball(1., 10., np.array([380.,20.]), np.array([-2.,2.])),Ball(1., 10., np.array([20.,380.]), np.array([2.,-2.]))]
    #ball_list = triangle_list()
    #ball_list.append(solver.Ball(10., 10., np.array([111.,100.]) , np.array([40.,40.])))
    #ball_list.append(solver.Ball(10., 10., np.array([380.,380.]) , np.array([-20.,-40.])))
    wlength = 400.
    step = 0.1
    display(ball_list, step, wlength)
    
                
    
