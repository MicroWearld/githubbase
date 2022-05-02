import pyGraph as pg
import statistic as s
from time import sleep

graph = pg.Graph()
graph.setup(570, 570)
pg.setresizable(graph, resizable=(0, 0))
pg.setaxis(graph, 0, 0, 6, 4)
pg.build_graph(graph, [18, 18], [1, 0.5], [0.04, 0.04],
               ruler=[1, 1], label=["x", "y"])
graph.tracer(1)
myfont = ("consolas", 15, "normal")
t = pg.domain(-2 * pg.pi, 2 * pg.pi, 0.01)
a = pg.vsin(10 * pg.pi * t) // 1 + 1
b = pg.vsin(0.5 * pg.pi * t) // 1 + 1
c = a * b
k = -2
try:
    pg.noted([0.5, -2.5], "red = green * purple", font=myfont)
    for i, j in {"green": a, "purple": b, "red": c}.items():
        p = pg.plot(t, j + k, c=i)
        k += 2
except pg.GraphInterrupt:
    print("GraphInterrupt")
print("done!")
graph.mainloop()
