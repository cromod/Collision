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

def create(balls, canvas):
    """Create a drawing item for each solver.Ball object
        
    balls the list of solver.Ball objects
    canvas the Tkinter.Canvas oject
    return a dictionary with solver.Ball objects as keys and their circle drawings as items
    """
    return {ball: canvas.create_circle(ball.position[0], ball.position[1], ball.radius, fill="white") for ball in balls}

def update(drawing, canvas, step, size):
    """Update the drawing items for a time step
        
    drawing the dictionary of drawing items
    canvas the Tkinter.Canvas oject
    step the time step
    size the medium size
    """
    balls = drawing.keys()
    solver.solve_step(balls, step, size)
    for ball in balls:
        canvas.coords_circle(drawing[ball], ball.position[0], ball.position[1], ball.radius)
    canvas.update()

def display(balls, step, size):
    """Display the simulation
        
    balls the list of solver.Ball objects
    step the time step
    size the medium size
    """
    # Instanciate the window, canvas and circle objects
    window = tk.Tk()
    window.poll = True
    canvas = tk.Canvas(window, width=size, height=size, bg="black")
    canvas.pack()
    canvas.focus_set()
    drawing = create(balls, canvas)
    # Define functions to launch and stop the simulation
    def animate():
        """Animate the drawing items"""
        if window.poll:
            update(drawing, canvas, step, size)
            window.after(0, animate)
        else:
            window.poll = True
    def stop():
        """Stop the animation"""
        window.poll = False
    # Define the buttons used to launch and stop the simulation
    start_button = tk.Button(window, text="Start", command=animate)
    stop_button = tk.Button(window, text="Pause", command=stop)
    start_button.pack()
    stop_button.pack()
    # GUI loop
    window.mainloop()

# Test this module
if __name__ == "__main__":
    balls = [solver.Ball(20., 20., [40.,40.], [5.,5.]), solver.Ball(10., 10., [480.,480.], [-15.,-15.]), solver.Ball(15., 15., [30.,470.], [10.,-10.])]
    size = 500.
    step = 0.1
    display(balls, step, size)
