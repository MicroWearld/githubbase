import os
class pgbar:
    def __init__(self,count,percentage=False):
        self.count=count
        self.percentage=percentage
        self.i=0
    def rise(self,loop,total):
        if total%self.count!=0:
            self.count=total
        if not self.percentage:
            if loop==0:
                print("progress:[",end="")
            if loop%(total//self.count)==0:
                print(">",end="")
            if loop==total-1:
                print("] done!")
        else:
            pc=str(round(loop/total*100))
            if loop%(total//self.count)==0:
                print("progress:["+">"*self.i+"."*(self.count-self.i)+"]",pc+"%")
                self.i+=1
            if loop==total-1:
                print("progress:["+">"*self.i+"."*(self.count-self.i)+"]","100%")
                print("done!")
                self.i=0
'''
简易进度条

使用方法：
from progresspar import pgbar
progressbar_name=pgbar(count,precentage=True/False) count:进度条的格数 percentage:是否开启百分比指示,默认为False
progressbar_name.rise(loop,total) 进度条前进 loop:当前循环数 total:总循环数
适用于已知执行次数的程序，便于用户查看进度

注意事项：
请尽量使总执行数能整除格数，否则格数会被自动设定为与总执行数相同的数字，无法体现用户自定义格数
'''

def test():#测试代码
    # count=int(input("请输入进度条格数："))
    count=100
    pb1=pgbar(count)
    pb2=pgbar(count,True)
    # total=int(input("请输入总循环数："))
    total=10000000
    print("无百分比指示：")
    for loop in range(total):
        pb1.rise(loop,total)
    print("有百分比指示：")
    for loop in range(total):
        pb2.rise(loop,total)

def quick(pbar,total):#快速测试
    for loop in range(total):
        pbar.rise(loop,total)
test()
input()