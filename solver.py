import numpy as np

class Ball:
    """Define physics of elastic collision."""
    
    def __init__(self, mass, radius, position, velocity):
        """Initialize a Ball object
        
        mass the mass of ball
        radius the radius of ball
        position the position vector of ball
        velocity the velocity vector of ball
        """
        self.mass = mass
        self.radius = radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.vafter = np.copy(velocity) # temporary storage for velocity of next step

    def compute_step(self, step):
        """Compute position of next step."""
        self.position += step * self.velocity
        
    def new_velocity(self):
        """Store velocity of next step."""
        self.velocity = self.vafter
        
    def computeEnergy(ball_list):
        """Compute kinetic energy."""
        return self.mass / 2. * np.linalg.norm(self.velocity)**2
    
    def compute_coll(self, ball, step):
        """Compute velocity after collision with another ball."""
        m1, m2 = self.mass, ball.mass
        r1, r2 = self.radius, ball.radius
        v1, v2 = self.velocity, ball.velocity
        x1, x2 = self.position, ball.position
        di = x2-x1
        norm = np.linalg.norm(di)
        if norm-r1-r2 < step*abs(np.dot(v1-v2, di))/norm:
            self.vafter = v1 - 2. * m2/(m1+m2) * np.dot(v1-v2, di) / (np.linalg.norm(di)**2.) * di

    def compute_refl(self, step, size):
        """Compute velocity after hitting an edge.

        step the step of computation
        size the size of a square edge
        """
        r, v, x = self.radius, self.velocity, self.position
        projx = step*abs(np.dot(v,np.array([1.,0.])))
        projy = step*abs(np.dot(v,np.array([0.,1.])))
        if abs(x[0])-r < projx or abs(size-x[0])-r < projx:
            self.vafter[0] *= -1
        if abs(x[1])-r < projy or abs(size-x[1])-r < projy:
            self.vafter[1] *= -1.


def solve_step(ball_list, step, size):
    """Solve a step for every ball."""
    
    # Detect edge-hitting and collision of every ball
    for ball1 in ball_list:
        ball1.compute_refl(step,size)
        for ball2 in ball_list:
            if ball1 is not ball2:
                ball1.compute_coll(ball2,step)
                
    # Compute position of every ball  
    for ball in ball_list:
        ball.new_velocity()
        ball.compute_step(step)