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


def maxheight(header): #Find maximum height
    if header == "":
        return 0

    return max(maxheight(header.left), maxheight(header.right)) + 1

def parent(header): #Find parent(nodethat containnextleft orright node)
    if header == "":
        return 0
    if header.left != "" or header.right != "":
        num_parent = 1
        node_parent.append(header.Val)
    else:
        num_parent = 0
    return parent(header.left) + parent(header.right) + num_parent

def children(header): #Find children(node that contain previous node)
    if header == "":
        return 0
    if header.left != "" or header.right != "":
        if header.right != "":
            num_children = 1
            node_childre.append(header.right.Val)
        if header.left != "" :
            num_children = 1
            node_childre.append(header.left.Val)
        if header.left != "" and header.right != "":
            num_children = 2
    else:
        num_children = 0
    return children(header.left) + children(header.right) + num_children

def leaves(header): #Findleaves(node that does not contain next left or right node)
    if header == "":
        return 0
    if header.left == "" and header.right == "":
        num_leaves = 1
        node_leaves.append(header.Val)
    else:
        num_leaves = 0
    return leaves(header.left) + leaves(header.right) + num_leaves

def sibling(header): #Find sibling(node that has the same parent)
    if header == "":
        return 0
    if header.left != "" and header.right != "":
        num_sibling = 1
        node_sibling.append([header.left.Val,header.right.Val])
    else:
        num_sibling = 0
    return sibling(header.left) + sibling(header.right) + num_sibling
            

header = Node(50)
arr_in = [25,75,30,60,40,35,70,90,15,45,27,55,85,100]
for inum in list(arr_in):
    header.append(inum)
arr_de = [30,75,35]
for inum in list(arr_de):
    header.delete(inum)

print("maximum height = " + str(maxheight(header)))
node_parent = []
print("parent = " + str(parent(header)) + " : " + str(node_parent))
node_childre = []
print("children = " + str(children(header)) + " : " + str(node_childre))
node_leaves = []
print("leaves = " + str(leaves(header)) + " : " + str(node_leaves))
node_sibling = []
print("sibling = " + str(sibling(header)) + " : " + str(node_sibling))

