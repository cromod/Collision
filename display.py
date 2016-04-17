import Tkinter as tk
import solver
import time
import sys

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _coords_circle(self, target, x, y, r, **kwargs):
    return self.coords(target, x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.coords_circle = _coords_circle

def draw(ball_list,canvas):
    draw_list = []
    for ball in ball_list:
        position = ball.position.tolist()
        draw_list.append(canvas.create_circle(position[0], position[1], ball.radius, fill="white"))
    return draw_list

def move(ball_list,draw_list,canvas):
    for i in range(len(ball_list)):
        position = ball_list[i].position.tolist()
        canvas.coords_circle(draw_list[i],position[0], position[1],ball_list[i].radius)

def stop(event):
    canvas.destroy()

def animation(ball_list, draw_list, canvas, step, wlength):
    flag = True
    while(flag):
        solver.solve_step(ball_list,step,wlength)
        move(ball_list,draw_list,canvas)
        canvas.update()
        #time.sleep(step)
        #canvas.bind('<KeyPress>', stop)

def run(ball_list, step, wlength):
    window = tk.Tk()
    canvas = tk.Canvas(window, width=wlength, height=wlength, bg="black")
    canvas.pack()
    draw_list = draw(ball_list,canvas)
    canvas.pack()
    canvas.focus_set()
    window.after(0,animation(ball_list, draw_list, canvas, step, wlength))
    window.mainloop()
