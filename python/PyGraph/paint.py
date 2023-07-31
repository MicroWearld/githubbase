import pyGraph as pg
import statistic as s
import random as r
import cmath as cm

graph = pg.Graph()
graph.setup(570, 570)
pg.setresizable(graph, resizable=(0, 0))
pg.setaxis(graph, 0, 2, 5, 5)
graph.delay(0)
pg.build_graph(graph, [10, 10], [1, 1], [0.08, 0.08], color="white",
               ruler=[1, 1], label=["x", "y"], delay=0, grid=False)
graph.tracer(0)
graph.bgcolor("black")
myfont = ("consolas", 15, "normal")
# -------------------------------------------------------------------
t = pg.domain(-2 * pg.pi, 2 * pg.pi, 0.01)
a = pg.vsin(20 * t) // 1 + 1
a_ = pg.vsin(200 * t) // 1 + 1
b = 1 * pg.vcos(1 * t)
c = (a * b).ifwhat(lambda x: x < 0, 0)
d = (a * b).ifwhat(lambda x: x > 0, 0)
e = 2 * a_
f = (a / b).ifwhat(lambda x: x > 0, 0)
sqw2 = pg.plot([t[0]], [d[0]], c="green")
sqw3 = pg.plot([t[0]], [c[0]], c="red")
sqw4 = pg.plot([t[0]], [e[0] - 3.5], c="blue")
sqw1 = pg.plot([t[0]], [f[0]], c="orange")
for i in range(1, len(t)):
    sqw1.draw(t[i], f[i])
    sqw2.draw(t[i], d[i])
    sqw3.draw(t[i], c[i])
    sqw4.draw(t[i], e[i] - 3.5)
# moon
moon = pg.plot(3 + pg.vcos(t), 5 + pg.vsin(t), c="silver", fill=True)
ellips = pg.plot(2.6 + pg.vcos(t), 5.4 + pg.vsin(t), c="black", fill=True)
moon.ht()
ellips.ht()
# cloud

graph.mainloop()
