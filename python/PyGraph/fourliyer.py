import pyGraph as pg
import statistic as s
import math as m

graph = pg.Graph()
graph.setup(570, 570)
pg.setresizable(graph, resizable=(0, 0))
pg.setaxis(graph, 0, 0, 10, 10)
pg.build_graph(graph, [100, 100], [1, 1], [0.08, 0.08],
               ruler=[1, 1], label=["x", "y"], delay=0, grid=False)
graph.tracer(1)
myfont = ("consolas", 15, "normal")
x = pg.domain(-10 * pg.pi, 10 * pg.pi, 0.01)

n = 10
r = 4
sita = list(range(-n - 1, n + 1))
sl = list(map(lambda n: s.integrate(lambda x: m.sin(
    2 * pg.pi * n * x / r) * (1 / 2 * x), 0, r) / r, sita))
cl = list(map(lambda n: s.integrate(lambda x: m.cos(
    2 * pg.pi * n * x / r) * (1 / 2 * x), 0, r) / r, sita))

y = 0
for i in range(len(sita)):
    y = y + cl[i] * pg.vcos(2 * pg.pi * sita[i] * x / r) + \
        sl[i] * pg.vsin(2 * pg.pi * sita[i] * x / r)

pg.plot(3 * y * pg.vcos(x), 3 * y * pg.vsin(x))
graph.mainloop()
