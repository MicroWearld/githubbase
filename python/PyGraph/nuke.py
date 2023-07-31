import pyGraph as pg
import math as m
import statistic as s

graph = pg.Graph()
graph.setup(570, 570)
pg.setresizable(graph, resizable=(0, 0))
pg.setaxis(graph, 0, 0, 2, 2)
pg.build_graph(graph, [18, 18], [0.5, 0.5], [0.04, 0.04],
               ruler=[1, 1], label=["x", "y"])
graph.tracer(1)
myfont = ("consolas", 15, "normal")
t = pg.domain(-pg.pi, pg.pi, 0.01)
l = pg.vsin(3 * t) // 1
try:
    n = pg.plot(pg.vcos(t), pg.vsin(t), c="yellow", fill=True)  # 画园
    u = pg.plot(l * pg.vcos(t), l * pg.vsin(t), c="black", fill=True)  # 画扇形
    k = pg.plot(0.2 * pg.vcos(t), 0.2 * pg.vsin(t),
                c="yellow", fill=True)  # 画外圆
    e = pg.plot(0.1 * pg.vcos(t), 0.1 * pg.vsin(t),
                c="black", fill=True)  # 画内圆
    for i in [n, u, k, e]:
        i.ht()
except pg.GraphInterrupt:
    print("GraphInterrupt")
print("done!")
graph.mainloop()
