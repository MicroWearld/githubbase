from core import *


class Mbutton(Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        Widget.__init__(self, master, 'button', cnf, kw)
        self.pos = ""
        self.mine = 0
        self.flag = 0
        self.cm = True


def cframe(size, num):
    global L2, Lnum, Ltime, root, m1
    root = Tk()
    root.resizable(False, False)
    root.geometry(size)
    win_image = PhotoImage(file='mymine.png')
    root.iconphoto(False, win_image)
    root.title("扫雷")
    root.bind("<Key-r>", lambda rubbish: truerst(Bsq, num))
    root.bind("<Key-q>", lambda rubbish: kill(root))
    root.bind("<Key-p>", lambda rubbish: stop(rubbish))
    L2 = Label(root, text="", font=("consolas", "25"))
    Lnum = Label(root, text=f"雷数:{num}", font=("consolas", "20"))
    Ltime = Label(root, text="Ready!", font=("consolas", "20"))
    mbar = Menu(root)
    m1 = Menu(mbar, tearoff=False)
    m1.add_command(label="重置", command=partial(fakerst, Bsq))
    m1.add_command(label="新游戏", command=partial(truerst, Bsq, num))
    m1.add_command(label="暂停/继续", command=partial(stop, 1))
    mbar.add_cascade(label="游戏", menu=m1)
    m2 = Menu(mbar, tearoff=False)
    m2.add_command(label="简单", command=partial(setdi, "easy"))
    m2.add_command(label="普通", command=partial(setdi, "normal"))
    m2.add_command(label="困难", command=partial(setdi, "hard"))
    mbar.add_cascade(label="难度", menu=m2)
    mbar.add_command(label="记录", command=showrecord)
    mbar.add_command(label="按键说明", command=tut)
    mbar.add_command(label="作者", command=author)
    root.config(menu=mbar)
    Lnum.place(anchor="nw", x=int(size.split("x")[0]) - 110, y=10)
    L2.pack(side="bottom")
    Ltime.place(anchor="nw", x=10, y=10)


def build(bsq, row, column):
    global tim
    tim = True
    del bsq[:]
    for i in range(row + 2):
        tmp = []
        for j in range(column + 2):
            butt = Mbutton(root, text="", width=3, height=1)
            butt["command"] = partial(showpos, butt)
            butt.bind("<3>", partial(setflag, (butt)))
            butt.pos = f"{i},{j}"
            tmp.append(butt)
        Bsq.append(tmp)


def placeB(bsq, row, column, left, top):
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            bsq[i][j].place(anchor="nw", x=left + (j - 1)
                            * 30, y=top + (i - 1) * 30)


def setdi(dif):
    global num, tnum, jnum, root
    left, top = 5, 60
    root.destroy()
    if dif == "easy":
        cframe("310x420", 10)
        num = tnum = jnum = 10
        build(Bsq, 10, 10)
        setmine(Bsq, num)
        placeB(Bsq, 10, 10, left, top)
    if dif == "normal":
        cframe("493x600", 40)
        num = tnum = jnum = 40
        build(Bsq, 16, 16)
        setmine(Bsq, num)
        placeB(Bsq, 16, 16, left, top)
    if dif == "hard":
        cframe("910x600", 99)
        num = tnum = jnum = 99
        build(Bsq, 16, 30)
        setmine(Bsq, num)
        placeB(Bsq, 30, 16, left, top)
    Lnum["text"] = f"雷数:{num}"
    root.mainloop()


def fakerst(bsq):
    global tnum, jnum, tim, tst
    tim = True
    tst = 0
    tnum = jnum = num
    Ltime.after_cancel(timee)
    m1.entryconfig(m1.index("暂停/继续"), state="active")
    root.bind("<Key-p>", lambda rubbish: stop(rubbish))
    Lnum["text"] = f"雷数:{num}"
    L2["text"] = ""
    Ltime["text"] = "Ready!"
    for i in range(1, len(bsq) - 1):
        for j in range(1, len(bsq[0]) - 1):
            bsq[i][j].flag = 0
            bsq[i][j].cm = True
            bsq[i][j].bind("<3>", partial(setflag, (bsq[i][j])))
            bsq[i][j]["text"] = ""
            bsq[i][j]["relief"] = "raised"
            bsq[i][j]["state"] = "normal"


def truerst(bsq, num):
    fakerst(bsq)
    for i in range(1, len(bsq) - 1):
        for j in range(1, len(bsq[0]) - 1):
            bsq[i][j].mine = 0
    setmine(bsq, num)


def setflag(butt, rubbish):
    global tnum, jnum
    pos = list(map(int, butt.pos.split(",")))
    if butt.flag == 0:
        butt["text"] = "%"
        butt["state"] = "disabled"
        butt.cm = False
        tnum -= 1
        if Bsq[pos[0]][pos[1]].mine == 1:
            jnum -= 1
    elif butt.flag == 1:
        butt["text"] = "?"
        butt["state"] = "disabled"
        tnum += 1
        if Bsq[pos[0]][pos[1]].mine == 1:
            jnum += 1
    else:
        butt.cm = True
        butt["text"] = ""
        butt["state"] = "normal"

    Lnum["text"] = f"雷数:{tnum}"
    butt.flag = (butt.flag + 1) % 3
    if tnum == jnum == 0:
        L2["text"] = "YOU WIN!"
        m1.entryconfig(m1.index("暂停/继续"), state="disabled")
        root.unbind("<Key-p>")
        Ltime.after_cancel(timee)
        B_lock(Bsq)
        checksc(num, round(des, 2))


def showpos(butt):
    global tim, start, Bsq
    pos = list(map(int, butt.pos.split(",")))
    if tim:
        start = time()
        if Bsq[pos[0]][pos[1]].mine == 1:
            rollmine(Bsq, pos)
        timing(Ltime, start)
        tim = False
    if Bsq[pos[0]][pos[1]].mine == 1:
        L2["text"] = "BOOM!YOU LOSE!"
        m1.entryconfig(m1.index("暂停/继续"), state="disabled")
        root.unbind("<Key-p>")
        Ltime.after_cancel(timee)
        butt["relief"] = "sunken"
        showmine(Bsq)
        B_lock(Bsq)
        return None
    if addc(Bsq, pos) == 0:
        showblank(Bsq, pos)
    else:
        butt["text"] = str(addc(Bsq, pos))
        butt["fg"] = colnum[addc(Bsq, pos)]
        butt.cm = False
        butt.bind("<Double-Button-1>", partial(search, pos))
    butt.unbind("<Button-3>")
    butt["relief"] = "sunken"
    if allblank(Bsq, jnum):
        L2["text"] = "YOU WIN!"
        m1.entryconfig(m1.index("暂停/继续"), state="disabled")
        root.unbind("<Key-p>")
        Ltime.after_cancel(timee)
        B_lock(Bsq)
        checksc(num, round(des, 2))


def timing(label, start):
    global des, timee
    H, M, S = 0, 0, 0
    cutime = time()
    des = cutime - start
    M = int(des // 60)
    S = round(des % 60, 2)
    label.config(text=f"{M}'{S}\"")
    timee = label.after(1, lambda: timing(label, start))


def search(pos, rubbish=1):
    ffl = False
    if addm(Bsq, pos) >= addc(Bsq, pos):
        for i in [pos[0] - 1, pos[0], pos[0] + 1]:
            for j in [pos[1] - 1, pos[1], pos[1] + 1]:
                if Bsq[i][j].flag == 0:
                    Bsq[i][j]["relief"] = "sunken"
                    Bsq[i][j].unbind("<3>")
                    if Bsq[i][j].mine == 1:
                        L2["text"] = "BOOM!YOU LOSE!"
                        m1.entryconfig(m1.index("暂停/继续"), state="disabled")
                        root.unbind("<Key-p>")
                        Ltime.after_cancel(timee)
                        showmine(Bsq)
                        B_lock(Bsq)
                        ffl = True
                        break
                    if 1 <= i <= len(Bsq) - 2 and 1 <= j <= len(Bsq[0]) - 2:
                        if addc(Bsq, [i, j]) == 0:
                            showblank(Bsq, [i, j])
                        else:
                            Bsq[i][j]["text"] = str(addc(Bsq, [i, j]))
                            Bsq[i][j]["fg"] = colnum[addc(Bsq, [i, j])]
                            Bsq[i][j].cm = False
                            Bsq[i][j].bind("<Double-Button-1>",
                                           partial(search, [i, j]))
            if ffl:
                break


def showblank(bsq, pos):
    i, j = pos
    bsq[i][j]["relief"] = "sunken"
    bsq[i][j].unbind("<3>")
    bsq[i][j].cm = False
    if addc(bsq, [i, j]) != 0:
        bsq[i][j]["text"] = str(addc(bsq, [i, j]))
        bsq[i][j]["fg"] = colnum[addc(bsq, [i, j])]
        bsq[i][j].bind("<Double-Button-1>", partial(search, [i, j]))
    else:
        if i != 1 and bsq[i - 1][j].cm:  # u
            showblank(bsq, [i - 1, j])
        if i != len(bsq) - 2 and bsq[i + 1][j].cm:  # d
            showblank(bsq, [i + 1, j])
        if j != 1 and bsq[i][j - 1].cm:  # l
            showblank(bsq, [i, j - 1])
        if j != len(bsq[0]) - 2 and bsq[i][j + 1].cm:  # r
            showblank(bsq, [i, j + 1])
        if bsq[i - 1][j - 1].cm and i != 1 and j != 1:  # u&l
            showblank(bsq, [i - 1, j - 1])
        if i != 1 and j != len(bsq[0]) - 2 and bsq[i - 1][j + 1].cm:  # u&r
            showblank(bsq, [i - 1, j + 1])
        if i != len(bsq) - 2 and j != 1 and bsq[i + 1][j - 1].cm:  # d&l
            showblank(bsq, [i + 1, j - 1])
        # d&r
        if i != len(bsq) - 2 and j != len(bsq[0]) - 2 and bsq[i + 1][j + 1].cm:
            showblank(bsq, [i + 1, j + 1])


def stop(rubbish):
    global st, st1, st2, tst
    if st:
        st1 = time()
        Ltime.after_cancel(timee)
        tB_lock(Bsq)
        for i in range(1, len(Bsq) - 1):
            for j in range(1, len(Bsq[0]) - 1):
                Bsq[i][j]["text"] = ""
                Bsq[i][j]["state"] = "disabled"
    else:
        st2 = time()
        tst += st2 - st1
        timing(Ltime, start + tst)
        for i in range(1, len(Bsq) - 1):
            for j in range(1, len(Bsq[0]) - 1):
                if Bsq[i][j].flag == 0:
                    Bsq[i][j]["state"] = "normal"
                if not Bsq[i][j].cm:
                    tmp = addc(Bsq, list(map(int, Bsq[i][j].pos.split(","))))
                    if tmp != 0:
                        Bsq[i][j]["text"] = tmp
                if Bsq[i][j].flag == 1:
                    Bsq[i][j]["text"] = "%"
                if Bsq[i][j].flag == 2:
                    Bsq[i][j]["text"] = "?"
                if Bsq[i][j].flag > 0 or Bsq[i][j].cm:
                    Bsq[i][j].bind("<3>", partial(setflag, (Bsq[i][j])))
    st = not st


row, column = 10, 10
num = tnum = jnum = 10
st = True
tst = st1 = sr2 = 0
Bsq = []

cframe("310x420", num)
build(Bsq, row, column)
setmine(Bsq, num)
placeB(Bsq, column, row, 5, 60)
root.mainloop()
