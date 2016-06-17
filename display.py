import Tkinter as tk
import solver

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _coords_circle(self, target, x, y, r, **kwargs):
    return self.coords(target, x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.coords_circle = _coords_circle

def initialize(balls, canvas):
    return [canvas.create_circle(ball.position[0], ball.position[1], ball.radius, fill="white") for ball in balls]

def move(balls, drawing, canvas):
    for i, ball in enumerate(balls):
        canvas.coords_circle(drawing[i], ball.position[0], ball.position[1], ball.radius)

def animate(balls, drawing, canvas, step, wlength):
    solver.solve_step(balls, step, wlength)
    move(balls, drawing, canvas)
    canvas.update()

def display(balls, step, wlength):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=wlength, height=wlength, bg="black")
    window.poll = True
    drawing = initialize(balls, canvas)
    
    def loop():
        if window.poll:
            animate(balls, drawing, canvas, step, wlength)
            window.after(0, loop)
        else:
            window.poll = True

    def stop():
        window.poll = False

    canvas.pack()
    canvas.focus_set()

    start_button = tk.Button(window, text="Start", command=loop)
    stop_button = tk.Button(window, text="Pause", command=stop)
    start_button.pack()
    stop_button.pack()

    window.mainloop()

# To test the module display
if __name__ == "__main__":
    balls = [solver.Ball(20., 20., [40.,40.], [5.,5.]), solver.Ball(10., 10., [480.,480.], [-15.,-15.]), solver.Ball(15., 15., [30.,470.], [10.,-10.])]
    wlength = 500.
    step = 0.1
    display(balls, step, wlength)
