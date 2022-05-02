class pgbar:
    def __init__(self,count,noclip=True):
        self.count=count
        self.noclip=noclip
        self.i=0
    def rise(self,loop,total):
        if total<self.count:
            print("please reset your count! It must be larger than total progress!")
        else:
            if self.noclip:
                if loop==0:
                    print("progress:[",end="")
                if loop%(total/self.count)==0:
                    print(">",end="")
                if loop==total-1:
                    print("] done!")
            else:
                pc=loop/total*100
                if loop%(total/self.count)==0:
                    print("progress:["+">"*self.i+"."*(self.count-self.i)+"]",str(round(pc))+"%")
                    self.i+=1
                if loop==total-1:
                    print("progress:["+">"*self.i+"."*(self.count-self.i)+"]","100%")
                    print("done!")
