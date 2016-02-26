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

def draw(ballList,canvas):
  drawList = []
  for ball in ballList:
    position = ball._position.tolist()
    drawList.append(canvas.create_circle(position[0], position[1], ball._radius, fill="white"))
  return drawList

def move(ballList,drawList,canvas):
  for i in range(len(ballList)):
    position = ballList[i]._position.tolist()
    canvas.coords_circle(drawList[i],position[0], position[1],ballList[i]._radius)

def stop(event):
  canvas.destroy()

def animation(ballList, drawList, canvas, step, wlength):
  flag = True
  while(flag):
    ballList = solver.solveStep(ballList,step,wlength)
    move(ballList,drawList,canvas)
    canvas.update()
    time.sleep(step)
    canvas.bind('<KeyPress>', stop)

def run(ballList, step, wlength):    
  window = tk.Tk()
  canvas = tk.Canvas(window, width=wlength, height=wlength, bg="black")
  canvas.pack()
  drawList = draw(ballList,canvas)
  canvas.pack()
  canvas.focus_set()
  window.after(0,animation(ballList, drawList, canvas, step, wlength))
  window.mainloop()