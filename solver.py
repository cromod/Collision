import numpy as np

class Ball:

    def __init__(self, mass, radius, position, velocity):
        self._mass = mass
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._vafter = np.copy(velocity)

    def compute_step(self, step, wlength):
        self._position += step * self._velocity
        
    def new_velocity(self):
        self._velocity = self._vafter
        
    def computeEnergy(ball_list):
        return self._mass*np.linalg.norm(self._velocity)**2
    
    def compute_coll(self, ball, step, wlength):
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

    def compute_refl(self, step, wlength):
        r = self._radius
        v = self._velocity
        x = self._position
        projx = step*abs(np.dot(v,np.array([1.,0.])))
        projy = step*abs(np.dot(v,np.array([0.,1.])))
        if abs(x[0])-r < projx or abs(wlength-x[0])-r < projx:
            self._vafter[0] *= -1
        if abs(x[1])-r < projy or abs(wlength-x[1])-r < projy:
            self._vafter[1] *= -1.

def solve_step(ball_list, step, wlength):
    ball_list = step1(ball_list, step, wlength)
    ball_list = step2(ball_list, step, wlength)
    return ball_list

def step1(ball_list, step, wlength):
    index_list = range(len(ball_list))
    for i in index_list:
        ball_list[i].compute_refl(step,wlength)
        for j in index_list:
            if i!=j:
                ball_list[i].compute_coll(ball_list[j],step,wlength)
    return ball_list

def step2(ball_list, step, wlength):
    index_list = range(len(ball_list)) 
    for i in index_list:
        ball_list[i].new_velocity()
        ball_list[i].compute_step(step,wlength)
    return ball_list

