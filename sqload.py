import sqlite3 as sql
import csv

db_path = "db.db"  # 数据库路径
csv_path = "hhh.csv"  # CSV文件路径
ctypes = ["INT", "INT"]  # 列类型
tablename = "hh"  # 表名称


def type_fomatter(string, typestr):
    if typestr == "INT":
        string = int(string)
    elif typestr == "TEXT":
        string = str(string)
    return string


def info(hb, strlist, ha):
    print(hb)
    for stri in strlist:
        print(stri)
    comfirm = input(ha)
    if comfirm.lower() == "y":
        return True
    else:
        return False


try:
    csvfile = open(csv_path)
    csviter = csv.reader(csvfile)
    columns = csviter.__next__()
    createstr = '''CREATE TABLE "{}" ('''.format(tablename)
    createlist = []
    executelist = []
    i = 0
    for col in columns:
        createlist.append("{} {}".format(col, ctypes[i]))
        i += 1
    createstr = createstr + ",".join(createlist) + ")"
    executelist.append(createstr)
    incertstr = '''INSERT INTO "{}" VALUES '''.format(tablename)
    for thing in csviter:
        rething = list(map(lambda s, t: type_fomatter(s, t), thing, ctypes))
        rething = str(rething).replace('[', '(').replace(']', ')')
        executelist.append(incertstr + rething)
    csvfile.close()
    if info("待执行SQL语句:", executelist, "确认(y):"):
        ddb = sql.connect(db_path)
        for exe in executelist:
            ddb.execute(exe)
            ddb.commit()
        print("执行成功!")
    else:
        print("终止!")
except Exception as be:
    print("数据库操作错误!", be)
