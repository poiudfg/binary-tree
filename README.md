# Binary tree from python
________________________________________________________________________________________________________________________________________________________ <br />
- [x] Insertion a new node function in binary tree
- [x] Sorted bumber (Adding node)
- [x] Deletion a node function in binary tree
- [x] Balance node function in binary tree 
- [x] Find maximum height
- [x] Find parent(nodethat containnextleft orright node)
- [x] Find children(node that contain previous node)
- [x] Find leaves(node that does not contain next left or right node)
- [x] Find sibling(node that has the same parent)
- [ ] <br />
__________________________________________________________________________________________________________________________________________________ <br />
 * function inside class:
```
class Node:
    def __init__(self,Val):
        self.Val = Val
        self.left = ""
        self.right = ""
```
> * Insertion a new node and Sorted bumber <br />
```
header.append(number)
```
```
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
```
> *  Deletion a node <br />
```
header.delete(number)
```
```

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
```
________________________________________________________________________________________________________________________________________________________ <br />
* function outside class:<br />
> * Balance node<br />
> > find inorder traversal first by code (inside class):
```
inorder = header.inorderTraversal(header)
```
```
def inorderTraversal(self, header):
            inorder = []
            if header:
                inorder = self.inorderTraversal(header.left)
                inorder.append(header.Val)
                inorder = inorder + self.inorderTraversal(header.right)
            return inorder
```
> code balance node
```
header = balance_tree(inorder,header)
```
```
def balance_tree_con(inorder,half,halftohalf,header):
    if header == "" or halftohalf == 0:
        return 0
    else:
        half_right = half + halftohalf
        half_left = half - halftohalf
        header.right = Node(inorder[half_right])
        header.left = Node(inorder[half_left])
        halftohalf = round(halftohalf/2)

    return balance_tree_con(inorder,half_left,halftohalf,header.left) + balance_tree_con(inorder,half_right,halftohalf,header.right)

def balance_tree(inorder,header):
    Len = len(inorder)
    half = round((Len-1) / 2)
    header = Node(inorder[half])
    halftohalf = round(half/2)
    balance_tree_con(inorder,half,halftohalf,header)

    return header
```
> * Find maximum height
```
print("maximum height = " + str(maxheight(header)))
```
```
def maxheight(header): #Find maximum height
    if header == "":
        return 0

    return max(maxheight(header.left), maxheight(header.right)) + 1
```
> * Find parent
```
node_parent = []
print("parent = " + str(parent(header)) + " : " + str(node_parent))
```
```
def parent(header): #Find parent(nodethat containnextleft orright node)
    if header == "":
        return 0
    if header.left != "" or header.right != "":
        num_parent = 1
        node_parent.append(header.Val)
    else:
        num_parent = 0
    return parent(header.left) + parent(header.right) + num_parent
```
> * Find children
```
node_childre = []
print("children = " + str(children(header)) + " : " + str(node_childre))
```
```
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
```
> * Find leaves
```
node_leaves = []
print("leaves = " + str(leaves(header)) + " : " + str(node_leaves))
```
```
def leaves(header): #Findleaves(node that does not contain next left or right node)
    if header == "":
        return 0
    if header.left == "" and header.right == "":
        num_leaves = 1
        node_leaves.append(header.Val)
    else:
        num_leaves = 0
    return leaves(header.left) + leaves(header.right) + num_leaves
```
> * Find sibling
```
node_sibling = []
print("sibling = " + str(sibling(header)) + " : " + str(node_sibling))
```
```
def sibling(header): #Find sibling(node that has the same parent)
    if header == "":
        return 0
    if header.left != "" and header.right != "":
        num_sibling = 1
        node_sibling.append([header.left.Val,header.right.Val])
    else:
        num_sibling = 0
    return sibling(header.left) + sibling(header.right) + num_sibling
```
