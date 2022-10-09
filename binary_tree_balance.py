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

def balance_tree_con(inorder,half,halftohalf,header):
    if header == "" or halftohalf == 0:
        return 0
    else:
        half_right = half + halftohalf
        half_left = half - halftohalf
        if half_right >= len(inorder):
            header.left = Node(inorder[half_left])
        else:
            header.right = Node(inorder[half_right])
            header.left = Node(inorder[half_left])
        halftohalf = round(halftohalf/2)

    return balance_tree_con(inorder,half_left,halftohalf,header.left) + balance_tree_con(inorder,half_right,halftohalf,header.right)

def balance_tree(inorder,header):
    Len = len(inorder)
    if Len % 2 == 0 :
        half = round(Len / 2)
    else:
        half = round((Len-1) / 2)
    header = Node(inorder[half])
    halftohalf = round(half/2)
    balance_tree_con(inorder,half,halftohalf,header)

    return header




header = Node(50)
arr_in = [25,75,30,60,40,35,70,90,15,45,27,55,85,100]
for inum in list(arr_in):
    header.append(inum)

arr_de = [30,75,35]
for inum in list(arr_de):
    header.delete(inum)

inorder = header.inorderTraversal(header)
print(inorder)
header = balance_tree(inorder,header)
