from tkinter import *
import os
from tkinter import filedialog
from change import change, rchange, wlt, twl
import tkinter.messagebox as tmb

p_encode, k_encode = "utf-8", "utf-8"


def get_file(eob):
    fpath = filedialog.askopenfilename(filetypes=[("ALL", "*")])
    if eob.get() != "":
        eob.delete(0, END)
    eob.insert(0, fpath)


def save_as_file(eob, tip, where=False):
    file = filedialog.asksaveasfile(defaultextension=".txt")
    if file != None:
        file.write(eob.get(1.0, END))
        file.close()
        if where:
            tip["text"] = "保\n存\n成\n功"
        else:
            tip["text"] = "保存成功"
    else:
        if where:
            tip["text"] = "保\n存\n成\n功"
        else:
            tip["text"] = "保存成功"


def adjust(string):
    if string[-1] == "\n":
        string = string[0:-1]
    return string


def search(st, j, k):
    if j % len(st) == 0 and j != 0:
        k += 1
    return st[j - len(st) * k], k


def jiami(mingwen, miyao):
    op = mingwen
    key = miyao
    j, k, check, sums = 0, 0, "", ""
    for i in op:
        pos, k = search(key, j, k)
        num = wlt[i] - wlt[pos]
        if num < 0:
            num = abs(num)
            check = check + "0"
            word = twl[num]
        else:
            check = check + "1"
            word = twl[num]
        sums = sums + word
        j += 1
    return sums, f"{key}${change(check)}"


def jeimi(miwen, gongyao):
    sums = miwen
    yek = gongyao
    yek = yek.split("$", 1)
    check = rchange(yek[1])
    check = check[len(check) - len(sums):]
    yek = yek[0]
    j, k, num, op = 0, 0, 0, ""
    for i in range(len(sums)):
        if check[i] == "0":
            num = 0 - wlt[sums[i]]
        else:
            num = wlt[sums[i]]
        pos, k = search(yek, j, k)
        rop = num + wlt[pos]
        op = op + twl[rop]
        j += 1
    return op.replace("§", "\n")


def Encrypt():
    if os.path.isfile(te.get()):
        pt = adjust(open(te.get(), encoding=p_encode).read()
                    ).replace("\n", "§")
    else:
        pt = te.get()
    if os.path.isfile(ke.get()):
        key = adjust(open(ke.get(), encoding=k_encode).read()
                     ).replace("\n", "")
    else:
        key = ke.get()
    if pt == "" or key == "":
        tip["text"] = "文本或密钥为空!"
        tip["fg"] = "red"
        return None
    try:
        res, public_key = jiami(pt, key)
    except KeyError as ker:
        tip["text"] = "存在非法字符: {}!".format(str(ker))
        tip["fg"] = "red"
        return None
    tip["text"] = "加密成功!"
    tip["fg"] = "green"
    Etop = Tk()
    Etop.resizable(0, 0)
    Etop.title("加密结果:")
    s1 = Scrollbar(Etop)
    s2 = Scrollbar(Etop)
    s1.pack(side="left", fill=Y)
    s2.pack(side="right", fill=Y)
    TEXT = Text(Etop, width=40, yscrollcommand=s1.set)
    PKEY = Text(Etop, width=40, yscrollcommand=s2.set)
    tips = Label(Etop)
    mbar = Menu(Etop)
    mbar.add_command(
        label="左:保存文本", command=lambda: save_as_file(TEXT, tips, True))
    mbar.add_command(
        label="右:保存公钥", command=lambda: save_as_file(PKEY, tips, True))
    TEXT.insert(1.0, res)
    PKEY.insert(1.0, public_key)
    TEXT.pack(side="left")
    PKEY.pack(side="right")
    tips.pack(side="bottom")
    Etop.config(menu=mbar)
    s1.config(command=TEXT.yview)
    s2.config(command=PKEY.yview)
    Etop.mainloop()


def Decrypt():
    if os.path.isfile(te.get()):
        pt = adjust(open(te.get(), encoding=p_encode).read())
    else:
        pt = te.get()
    if os.path.isfile(ke.get()):
        key = adjust(open(ke.get(), encoding=k_encode).read())
    else:
        key = ke.get()
    if pt == "" or key == "":
        tip["text"] = "文本或密钥为空!"
        tip["fg"] = "red"
        return None
    try:
        res = jeimi(pt, key)
    except IndexError as ie:
        if "list" in str(ie):
            tip["text"] = "公钥格式错误!"
            tip["fg"] = "red"
        elif "string" in str(ie):
            tip["text"] = "公钥长度错误!"
            tip["fg"] = "red"
        return None
    except KeyError as ker:
        tip["text"] = "存在非法字符: {}!".format(str(ker))
        tip["fg"] = "red"
        return None
    tip["text"] = "解密成功!"
    tip["fg"] = "green"
    Etop = Tk()
    Etop.resizable(0, 0)
    Etop.title("解密结果:")
    sb = Scrollbar(Etop)
    sb.pack(side="right", fill=Y)
    TEXT = Text(Etop, yscrollcommand=sb.set)
    tips = Label(Etop)
    mbar = Menu(Etop)
    mbar.add_command(label="保存文本", command=lambda: save_as_file(TEXT, tips))
    TEXT.insert(1.0, res)
    TEXT.pack()
    tips.pack(side="bottom")
    Etop.config(menu=mbar)
    sb.config(command=TEXT.yview)
    Etop.mainloop()


win_width, win_height = 300, 80
root = Tk()
root.title("加解密程序")
root.resizable(False, False)
root.geometry("{}x{}+400+150".format(win_width, win_height))
text = Label(root, text="文本:")
key = Label(root, text="密钥:")
tip = Label(root, text="")
te = Entry(root)
ke = Entry(root)
tb = Button(root, text="...", command=lambda: get_file(te))
kb = Button(root, text="...", command=lambda: get_file(ke))
encrypt = Button(root, text="加密", command=Encrypt)
decrypt = Button(root, text="解密", command=Decrypt)
text.place(x=0, y=0, anchor="nw")
key.place(x=0, y=win_height / 2, anchor="w")
tip.place(x=40, y=win_height - 2, anchor="sw")
te.place(x=40, y=0, anchor="nw")
ke.place(x=40, y=win_height / 2, anchor="w")
tb.place(x=186, y=0, anchor="nw", height=21)
kb.place(x=186, y=win_height / 2, anchor="w", height=21)
encrypt.place(x=220, y=win_height / 3, anchor="w", height=25, width=70)
decrypt.place(x=220, y=win_height / 3 * 2, anchor="w", height=25, width=70)
root.mainloop()
