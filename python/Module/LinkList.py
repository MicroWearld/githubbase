class linknode:
    def __init__(self,data_,next_=None):
        self.data=data_
        self.next=next_

class linklist:
    def __init__(self):
        self.head=None

    def __len__(self):
        time=0
        cur=self.head
        while cur is not None:
                time+=1
                cur=cur.next
        return time

    def __str__(self):
        s=""
        cur=self.head
        while cur is not None:
            s+=f"{cur.data}->"
            cur=cur.next
        return s[:-2]
    
    def __repr__(self):
        s=""
        cur=self.head
        while cur is not None:
            s+=f"{cur.data}->"
            cur=cur.next
        return s[:-2]

    def prepend(self,data_):
        if self.head is None:
            self.head=linknode(data_)
        else:
            self.head=linknode(data_,self.head)
    
    def append(self,data_):
        if self.head is None:
            self.head=linknode(data_)
        else:
            pre=self.head
            while pre.next is not None:
                pre=pre.next
            pre.next=linknode(data_)
    
    def insert(self,index,data_):
        if index<0:
            index+=len(self)+1
        if len(self)==0 or index<0 or index>=len(self):
            self.append(data_)
        elif index==0:
            self.prepend(data_)
        else:
            pre=self.head
            while index>1:
                pre=pre.next
                index-=1
            pre.next=linknode(data_,pre.next)

    def pop(self,index=-1):
        if self.head is None:
            raise OverflowError("EMPTY LINKLIST")
        if index<0:
            index+=len(self)
        if index<0 or index>=len(self):
            index=len(self)-1
        if index==0:
            self.head=self.head.next
        else:
            pre=self.head
            while index>1:
                index-=1
                pre=pre.next
            pre.next=pre.next.next
