from urllib.parse import quote
from flask import Flask, render_template, send_from_directory, request, abort, make_response
from core import *

server = Flask(__name__)
sp = os_pathsp()
working = os.listdir(os.getcwd())
regstr = ""
targetpath = os.getcwd()


def download(src):
    filename = os.path.join(os.getcwd(), src)
    src = src.split(sp)[-1]
    response = make_response(send_from_directory(
        filename.replace(src, ""), src))
    basename = os.path.basename(filename)
    response.headers["Content-Disposition"] = \
        "attachment;" \
        "filename*=UTF-8''{utf_filename}".format(
            utf_filename=quote(basename.encode('utf-8'))
    )
    return response


@server.route("/webfont/sarasa-mono-sc-nerd-regular.ttf")
def sarasa():
    return send_from_directory(server.root_path + f"{sp}templates{sp}webfont", "sarasa-mono-sc-nerd-regular.ttf")


@server.route("/webfont/DejaVuSansMono.ttf")
def dejavu():
    return send_from_directory(server.root_path + f"{sp}templates{sp}webfont", "DejaVuSansMono.ttf")


@server.route("/css/index.css")
def indexcss():
    return send_from_directory(server.root_path + f"{sp}templates{sp}css", "index.css")


@server.route("/favicon.ico")
def favicon():
    return send_from_directory(server.root_path + "\\templates\\icon", "cmd.ico")


@server.route("/target", methods=["POST", "GET"])
def target():
    global targetpath
    targetdir = os.listdir(targetpath)
    info, color = "", "green"
    if request.method == "POST":
        try:
            option = request.form.get("rop")
            item = request.form.getlist("rcb")
            detail = request.form.get("rnapore")
            print(option, item, detail)
            if option != "刷新":
                if option == "前进":
                    _targetpath = (targetpath + sp + targetdir[int(item[0])])
                    info = "目录切换成功!"
                elif option == "后退":
                    _targetpath = back(targetpath)
                    info = "目录退档成功!"
                elif option == "跳转":
                    os.listdir(detail)
                    _targetpath = detail
                    info = "目录跳转成功!"
                _targetpath = os.path.abspath(_targetpath)
                os.listdir(_targetpath)
                targetpath = _targetpath
        except IndexError:
            info, color = "未选择前进目录", "red"
        except BaseException as e:
            info, color = str(e), "red"
    return render_template("target.html", screen=escape(show_dict(targetpath, opt=["what", "self"])), info=info, color=color, pwd=targetpath)


@server.route("/", methods=["POST", "GET"])
def index():
    global regstr, working, ck, targetpath
    info, color, ck = "", "green", ""
    if request.method == "GET":
        working = os.listdir()
        screen = show_dict()
        return render_template("index.html", user="Wang", screen=escape(show_dict()),
                               pwd=os.getcwd(), info="", color=color)
    else:
        if list(request.form) == []:
            try:
                flt = request.files.getlist("file")
                server.config["UPLOAD_FOLDER"] = os.getcwd()
                for f in flt:
                    f.save(os.path.join(
                        server.config['UPLOAD_FOLDER'], myfilename(f.filename)))
                fi = ",".join(list(map(lambda x: x.filename, flt)))
                info = fi + " 上传成功!"
            except BaseException as err:
                info, color = str(err), "red"
            finally:
                working = os.listdir()
                screen = escape(show_dict())
        else:
            option = request.form.get("op")
            item = request.form.getlist("cb")
            detail = request.form.get("napore")
            print(option, item, detail)
            if option == "下载":
                if len(item) == 0:
                    info, color = "未选择下载项", "red"
                else:
                    return download(os.path.join(os.getcwd(), working[int(item[0])]))
            elif option == "新建文件夹":
                try:
                    os.mkdir(os.path.join(os.getcwd(), detail))
                except BaseException as Err:
                    info, color = str(Err), "red"
                else:
                    info = "{} 创建成功!".format(detail)
            elif option == "删除":
                if len(item) == 0:
                    info, color = "未选择删除项!", "red"
                else:
                    try:
                        delist = list(map(lambda x: working[int(x)], item))
                        for di in delist:
                            di = os.path.join(os.getcwd(), di)
                            if os.path.isdir(di):
                                shutil.rmtree(di)
                            else:
                                os.remove(di)
                    except BaseException as err:
                        info, color = str(err), "red"
                    else:
                        info = "{} 删除成功!".format(
                            str(delist)[1:-1])
            elif option == "复制":
                if len(item) == 0:
                    info, color = "未选择复制项!", "red"
                else:
                    try:
                        delist = list(map(lambda x: working[int(x)], item))
                        for di in delist:
                            if os.path.isdir(di):
                                shutil.copytree(di, os.path.join(
                                    targetpath, di))
                            else:
                                shutil.copy2(di, os.path.join(
                                    targetpath, di))
                    except BaseException as e:
                        info, color = str(e), "red"
                    else:
                        info = "{} 复制成功!".format(str(delist)[1:-1])
            elif option == "移动":
                if len(item) == 0:
                    info, color = "未选择移动项!", "red"
                else:
                    try:
                        delist = list(map(lambda x: working[int(x)], item))
                        for di in delist:
                            shutil.move(di, os.path.join(
                                targetpath, di))
                    except BaseException as e:
                        info, color = str(e), "red"
                    else:
                        info = "{} 移动成功!".format(str(delist)[1:-1])
            elif option == "重命名":
                if len(item) != 1 or detail == "":
                    info, color = "无法重命名!", "red"
                else:
                    try:
                        de = os.path.join(os.getcwd(), working[int(item[0])])
                        os.rename(de, detail)
                    except BaseException as e:
                        info, color = str(e), "red"
                    else:
                        info = "{} 重命名成功!".format(working[int(item[0])])
            elif option == "压缩":
                if len(item) == 0:
                    info, color = "未选择压缩项!", "red"
                else:
                    try:
                        delist = list(map(lambda x: working[int(x)], item))
                        for di in delist:
                            dic = os.path.join(os.getcwd(), di)
                            if os.path.isdir(dic):
                                shutil.make_archive(di, "zip", dic)
                            else:
                                raise LogicalError("{} 不是文件夹!".format(di))
                    except BaseException as e:
                        info, color = str(e), "red"
                    else:
                        info = "{} 压缩成功!".format(str(delist)[1:-1])
            elif option == "前进":
                try:
                    os.listdir(os.getcwd() + sp + working[int(item[0])])
                    os.chdir(os.getcwd() + sp + working[int(item[0])])
                    info = "目录切换成功!"
                except IndexError:
                    info, color = "未选择前进目录!", "red"
                except BaseException as e:
                    info, color = str(e), "red"
            elif option == "后退":
                try:
                    os.chdir(back(os.getcwd()))
                    info = "目录退档成功!"
                except BaseException as e:
                    info, color = str(e), "red"
            elif option == "跳转":
                try:
                    os.chdir(detail)
                    info = "目录跳转成功!"
                except BaseException as e:
                    info, color = str(e), "red"
            elif option == "交换":
                temp = os.getcwd()
                os.chdir(targetpath)
                targetpath = temp
                info = "目录交换成功!"
            if request.form.get("reg"):
                try:
                    if detail != "":
                        regstr = detail
                    working = reg_check(regstr, os.listdir())
                    screen = escape(show_dict(pat=regstr))
                    info = "筛选成功!"
                    ck = "checked"
                except BaseException as e:
                    working = os.listdir()
                    screen = escape(show_dict())
                    regstr = ""
                    info, color = str(e), "red"
            else:
                working = os.listdir()
                screen = escape(show_dict())
                regstr = ""

        return render_template("index.html", user="Wang", screen=screen,
                               pwd=os.getcwd(), info=info, color=color, ck=ck)


if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True)
