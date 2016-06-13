import Tkinter as tk
import solver

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _coords_circle(self, target, x, y, r, **kwargs):
    return self.coords(target, x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.coords_circle = _coords_circle

def display(balls, canvas):
    return [canvas.create_circle(ball.position[0], ball.position[1], ball.radius, fill="white") for ball in balls]

def move(balls, drawing, canvas):
    for i, ball in enumerate(balls):
        canvas.coords_circle(drawing[i], ball.position[0], ball.position[1], ball.radius)

def stop(event):
    canvas.destroy()

def animation(balls, drawing, canvas, step, wlength):
    flag = True
    while(flag):
        solver.solve_step(balls, step, wlength)
        move(balls, drawing, canvas)
        canvas.update()
        #time.sleep(step)
        #canvas.bind('<KeyPress>', stop)

def run(balls, step, wlength):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=wlength, height=wlength, bg="black")
    canvas.pack()
    drawing = display(balls, canvas)
    canvas.pack()
    canvas.focus_set()
    window.after(0, animation(balls, drawing, canvas, step, wlength))
    window.mainloop()
