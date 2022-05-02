__all__ = ["BinaryTree", "sort_tree"]


class BinaryTree:
    '''根据treelist生成二叉树:
    treelist:生成列表
    mode:方法设置(array,list,recursion)
         array:按照层序遍历的数组生成二叉树
         list:按照嵌套列表生成二叉树
         recursion:树嵌套生成(程序式生成,不建议直接使用)
    '''

    def __init__(self, treelist, c=0, mode="recursion"):
        if mode == "array":
            self.root = treelist[c]
            if (c + 1) * 2 - 1 <= len(treelist) - 1 and treelist[(c + 1) * 2 - 1] != None:
                self.left = BinaryTree(treelist, (c + 1) * 2 - 1, mode="array")
            else:
                self.left = None
            if (c + 1) * 2 <= len(treelist) - 1 and treelist[(c + 1) * 2] != None:
                self.right = BinaryTree(treelist, (c + 1) * 2, mode="array")
            else:
                self.right = None
        elif mode == "list":
            self.root = treelist[0]
            if isinstance(treelist[1], list):
                self.left = BinaryTree(treelist[1], mode="list")
            elif treelist[1] != None:
                self.left = BinaryTree([treelist[1], None, None], mode="list")
            else:
                self.left = None
            if isinstance(treelist[2], list):
                self.right = BinaryTree(treelist[2], mode="list")
            elif treelist[2] != None:
                self.right = BinaryTree([treelist[2], None, None], mode="list")
            else:
                self.right = None
        elif mode == "recursion":
            self.root, self.left, self.right = treelist
        else:
            raise AttributeError(
                "The mode must be 'list' 'array' or 'recursion' !")

    def VLR(self):
        '''返回前序遍历列表'''
        def _VLR(BT, s=[]):
            s.append(BT.root)
            if BT.left != None:
                _VLR(BT.left, s)
            if BT.right != None:
                _VLR(BT.right, s)
            return s

        s = []
        return _VLR(self, s)

    def LDR(self):
        '''返回中序遍历列表'''
        def _LDR(BT, s=[]):
            if BT.left != None:
                _LDR(BT.left, s)
            s.append(BT.root)
            if BT.right != None:
                _LDR(BT.right, s)
            return s

        s = []
        return _LDR(self, s)

    def LRD(self):
        '''返回后序遍历列表'''
        def _LRD(BT, s=[]):
            if BT.left != None:
                _LRD(BT.left, s)
            if BT.right != None:
                _LRD(BT.right, s)
            s.append(BT.root)
            return s

        s = []
        return _LRD(self, s)

    def search(self, data):
        '''查找数据,输入待查节点数据,
             若查找成功,返回从根节点开始到待查节点数据的路径列表
             否则,返回None
        '''
        v = self.VLR()
        rl = self.LRD()[::-1]
        if data not in v:
            return None
        else:
            rl = rl[rl.index(data) + 1:]
            for i in range(len(rl)):
                v.pop(v.index(rl[i]))
            v = v[0:v.index(data) + 1]
            step, node = [], self
            for i in v:
                if node.root != None and node.left.root == i:
                    step.append(0)
                    node = node.left
                elif node.root != None and node.right.root == i:
                    step.append(1)
                    node = node.right
            return step

    def step(self, step):
        '''步进数据:输入路径,返回对应节点数据'''
        node = self
        for i in step:
            if i == 0:
                node = node.left
            elif i == 1:
                node = node.right
            else:
                raise AttributeError("step list Error!")
        if node == None:
            return None
        return node.root

    def replace(self, step, change, mode=None):
        '''替换数据:输入路径和数据，替换原路径的数据
            若mode为None,只替换节点数据
            若mode为方法参数,则替换整棵子树'''
        node = self
        if mode == None:
            for i in step:
                if i == 0:
                    node = node.left
                else:
                    node = node.right
            node.root = change
        else:
            for i in step[:-1]:
                if i == 0:
                    node = node.left
                else:
                    node = node.right
            if step[-1] == 0:
                node.left = BinaryTree(change, mode=mode)
            else:
                node.right = BinaryTree(change, mode=mode)

    def pop(self, step):
        '''删除数据:输入路径,删除对应的子树'''
        node = self
        for i in step[:-1]:
            if i == 0:
                node = node.left
            elif i == 1:
                node = node.right
            else:
                raise AttributeError("step list Error!")
        if step[-1] == 0:
            del node.left.left, node.left.right
            node.left = None
        elif step[-1] == 1:
            del node.right.left, node.right.right
            node.right = None
        else:
            raise AttributeError("step list Error!")


def sort_tree(data):
    '''输入待排序列表,生成二叉排序(查找)树'''
    sort = BinaryTree([data[0], None, None])
    for d in data[1:]:
        temp = sort
        while True:
            if d <= temp.root:
                if temp.left == None:
                    temp.left = BinaryTree([d, None, None])
                    break
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = BinaryTree([d, None, None])
                    break
                else:
                    temp = temp.right
    return sort

#--------------------------TEST------------------------------


# bt, n = BinaryTree, None
# t1 = bt([1, 2, 3, 4, 5, 6, 7], mode="array")
# t2 = bt([1, [2, [4, n, n], [5, n, n]], [3, [6, n, n], [7, n, n]]], mode="list")
# t3 = bt([1, bt([2, bt([4, n, n]), bt([5, n, n])]),
#          bt([3, bt([6, n, n]), bt([7, n, n])])], mode="recursion")

# for i in [t1, t2, t3]:
#     print(i.VLR(), i.LDR(), i.LRD())

# sort = sort_tree([3, 1, 7, 8, 9, 0, 2, 4, 6, 5])
# print(sort.LDR())
