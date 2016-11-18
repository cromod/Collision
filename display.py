import Tkinter as tk
import solver

def _create_circle(self, x, y, r, **kwargs):
    """Create a circle
        
    x the abscissa of centre
    y the ordinate of centre
    r the radius of circle
    **kwargs optional arguments
    return the drawing of a circle
    """
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _coords_circle(self, target, x, y, r, **kwargs):
    """Define a circle
        
    target the circle object
    x the abscissa of centre
    y the ordinate of centre
    r the radius of circle
    **kwargs optional arguments
    return the circle drawing with updated coordinates
    """
    return self.coords(target, x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.coords_circle = _coords_circle

class Display:
    """Define the window used to display a simulation"""
    
    def __init__(self, balls, step, size):
        """Initialize and launch the display"""
        self.balls = balls
        self.step = step
        self.size = size
        
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=self.size, height=self.size, bg="black")
        self.canvas.pack()
        self.canvas.focus_set()
        self.drawing = self.create()
        self.started = False
    
        start_button = tk.Button(self.window, text="Start", command=self.start)
        stop_button = tk.Button(self.window, text="Pause", command=self.stop)
        start_button.pack()
        stop_button.pack()
    
        self.window.mainloop()
    
    def create(self):
        """Create a drawing item for each solver.Ball object
            
        return a dictionary with solver.Ball objects as keys and their circle drawings as items
        """
        return {ball: self.canvas.create_circle(ball.position[0], ball.position[1], ball.radius, fill="white") for ball in self.balls}

    def update(self):
        """Update the drawing items for a time step"""
        solver.solve_step(self.balls, self.step, self.size)
        for ball in self.balls:
            self.canvas.coords_circle(self.drawing[ball], ball.position[0], ball.position[1], ball.radius)
        self.canvas.update()

    def start(self):
        """Start the animation"""
        if not self.started:
            self.started = True
            self.animate()

    def animate(self):
        """Animate the drawing items"""
        if self.started:
            self.update()
            self.window.after(0, self.animate)

    def stop(self):
        """Stop the animation"""
        self.started = False

# Test this module
if __name__ == "__main__":
    balls = [solver.Ball(20., 20., [40.,40.], [5.,5.]), solver.Ball(10., 10., [480.,480.], [-15.,-15.]), solver.Ball(15., 15., [30.,470.], [10.,-10.])]
    size = 500.
    step = 0.01
    Display(balls, step, size)
