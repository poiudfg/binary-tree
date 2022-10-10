class Node:
    def __init__(self,Val):
        self.Val = Val
        self.left = ""
        self.right = ""
        
    def append(self,Val):
        while True:
            if Val > self.Val:
                if self.right == "":
                    self.right = Node(Val)
                    break
                else:
                    self = self.right

            if Val < self.Val:
                if self.left  == "":
                    self.left = Node(Val)
                    break
                else:
                    self = self.left
                    
    def delete(self,Val):
        while True:
            if Val > self.Val:
                if self.right.Val == Val:
                    pre_temp = self
                    
                self = self.right
                    
            if Val < self.Val:
                if self.left.Val == Val:
                    pre_temp = self
                    
                self = self.left
            if Val == self.Val:
                break
        
        if self.right != "":
            temp = self.right
            if temp.left != "":
                while True:
                    if temp.left.left == "":
                        temp2 = temp.left.right
                        temp.left.left = self.left
                        temp.left.right = self.right
                        self = temp.left
                        temp.left = temp2
                        break
                    else:
                        temp = temp.left
            else:
                temp.left = self.left
                self = temp
                
        elif self.left != "" and self.right == "":
            self = self.left
            
        elif self.right == "" and self.left == "":
            self = ""
            
        if pre_temp.right != "":
            if pre_temp.right.Val == Val:
                pre_temp.right = self
        if pre_temp.left.Val == Val:
            pre_temp.left = self

    def inorderTraversal(self, header):
            inorder = []
            if header:
                inorder = self.inorderTraversal(header.left)
                inorder.append(header.Val)
                inorder = inorder + self.inorderTraversal(header.right)
            return inorder

    
def con_balance(nodes,start,end):
    if start > end:
        return ""
    mid=(start+end)//2
    header = Node(nodes[mid])

    header.left = con_balance(nodes,start,mid-1)
    header.right = con_balance(nodes,mid+1,end)

    return header
    
    
def balance_tree(header):
    nodes = header.inorderTraversal(header) #inorder
    Len = len(nodes)

    return con_balance(nodes,0,Len-1)



header = Node(1)
arr_in = [2,3,4,5,6,7]
for inum in list(arr_in):
    header.append(inum)

arr_de = []
for inum in list(arr_de):
    header.delete(inum)

header = balance_tree(header)
header.append(13)
header.append(14)
inorder = header.inorderTraversal(header)
header = balance_tree(header)
print()