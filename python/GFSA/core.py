from random import randint
import time
import stat
import shutil
import os
import string
import re
import uuid


class LogicalError(Exception):
    pass


def reg_check(pat, seq):

    def regcacul(patlist, st):
        stack = []
        i = 0
        try:
            while i < len(patlist):
                if "/" in patlist[i]:
                    stack.append(re.search(re.compile(patlist[i][1:-1]), st))
                elif "/" not in patlist[i] and patlist[i] != "!" and patlist[
                        i] != "|" and patlist[i] != "&":
                    raise LogicalError("无效正则表达式,请将它放在'//'内!")
                if patlist[i] == "!":
                    stack[-1] = not stack[-1]
                elif patlist[i] == "&":
                    temp = stack.pop()
                    stack[-1] = stack[-1] and temp
                elif patlist[i] == "|":
                    temp = stack.pop()
                    stack[-1] = stack[-1] or temp
                i += 1
        except IndexError:
            raise LogicalError("表达式有误,请确认是否为逆波兰表达式!")
        if len(stack) != 1:
            raise LogicalError("表达式未结束!")
        return stack[0]

    if pat == None:
        return seq
    else:
        ppat = pat.split(" ")
        seq = list(filter(lambda st: regcacul(ppat, st), seq))
        return seq


def search_letter(string):
    al, nal = 0, 0
    for s in string:
        if s.isascii():
            al += 1
        else:
            nal += 1
    return [al, nal, len(string)]


def format_time(tmt, mode):
    ti = time.localtime(tmt)
    if mode == "1":
        ft = f"{ti[0]}年{ti[1]}月{ti[2]}日"
    else:
        ft = f"{ti[3]}:{ti[4]}:{ti[5]}"
    return ft


def format_size(size):
    if size < 1024:
        fsize = f"{size}B"
    elif size < 1024**2:
        fsize = f"{round(size/1024,2)}KB"
    elif size < 1024**3:
        fsize = f"{round(size/(1024**2),2)}MB"
    else:
        fsize = f"{round(size/(1024**3),2)}GB"
    return fsize


def get_fst(fpath, file, mode):
    try:
        f = file
        fpath = os.path.join(os.getcwd(), fpath)
        file = os.path.join(fpath, file)
        if mode == "what":
            if os.path.isdir(file):
                res = "<DIR>"
            elif os.path.isfile(file):
                res = "<FLE>"
            elif os.path.islink(file):
                res = "<LNK>"
            elif os.path.ismount(file):
                res = "<MNT>"
            else:
                res = "<ERR>"
        elif mode == "size":
            res = format_size(os.stat(file).st_size)
        elif mode == "mtime1":
            res = format_time(os.stat(file).st_mtime, "1")
        elif mode == "mtime2":
            res = format_time(os.stat(file).st_mtime, "2")
        elif mode == "self":
            res = f
    except FileNotFoundError as err:
        res = str(err)
    return str(res)


def escape(string):
    res = string.replace(" ", "&nbsp;")
    res = res.replace("<", "&lt;")
    res = res.replace(">", "&gt;")
    return res


def myfilename(name):
    res = name
    for notallow in ["/", "\\", "<", ">", "?"]:
        res = res.replace(notallow, "")
    return res


def back(path):
    pl = path.split("\\")
    bp = "\\".join(pl[:-1]) + "\\"
    return bp


def os_pathsp():
    if os.name == "nt":
        return "\\"
    elif os.name == "posix":
        return "/"


def show_dict(fpath=".",
              opt=["mtime1", "mtime2", "what", "size", "self"],
              formatnum={
                  "what": 9,
                  "mtime1": 18,
                  "mtime2": 12,
                  "size": 12
              },
              pat=None):
    try:
        n = len(os.listdir(fpath))
        dictlist = reg_check(pat, os.listdir(fpath))
    except FileNotFoundError as err:
        return str(err) + "\n" + show_dict()
    else:
        rstr, res = "", f"total:{n}    showed:{len(dictlist)}\n"
        for part in dictlist:
            for p in opt:
                thing = get_fst(fpath, part, p)
                if p == "self":
                    rstr += (">" + thing)
                else:
                    rstr += (thing + " " *
                             (formatnum[p] - search_letter(thing)[0] -
                              search_letter(thing)[1] * 2))
            res += (rstr + "\n")
            rstr = ""
        return res
