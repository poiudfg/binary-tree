# Binary tree from python
---
- [x] Insertion a new node function in binary tree
- [x] Sorted bumber (Adding node)
- [x] Deletion a node function in binary tree
- [x] Balance node function in binary tree 
- [x] Find maximum height
- [x] Find parent (nodethat containnextleft orright node)
- [x] Find children (node that contain previous node)
- [x] Find leaves (node that does not contain next left or right node)
- [x] Find sibling (node that has the same parent)
- [ ] ...
---
 * function inside class :
```
class Node:
    def __init__(self,Val):
        self.Val = Val
        self.left = ""
        self.right = ""
```
code Insertion a new node and Sorted bumber :
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
* diagrams Insertion a new node and Sorted bumber Ex:
```mermaid
graph TD;
    5-->3;
    5-->7;
    3-->4;
```
> add number 2 :
```mermaid
graph TD;
    5-->3;
    5-->7;
    3-->2;
    3-->4;
```
---
Deletion a node <br />
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
        if pre_temp.left != "":
            if pre_temp.left.Val == Val:
                pre_temp.left = self
```
* diagrams deletion a node Ex:
```mermaid
graph TD;
    50-->25;
    50-->75;
    25-->15;
    25-->30;
    30-->27;
    30-->40;
    75-->90;
    75-->60;
    90-->85;
```
> case 1 (right -> left) delete number 25 :
```mermaid
graph TD;
    50-->27;
    50-->75;
    27-->15;
    27-->30;
    30-->40;
    75-->90;
    75-->60;
    90-->85;
```
> case 2 (right) delete number 75 :
```mermaid
graph TD;
    50-->27;
    50-->90;
    27-->15;
    27-->30;
    30-->40;
    90-->60;
    90-->85;
```
> case 3 (left only) delete number 90 :
```mermaid
graph TD;
    50-->27;
    50-->75;
    27-->15;
    27-->30;
    30-->40;
    75-->85;
    75-->60;
```
> case 4 (no children) delete number 15 :
```mermaid
graph TD;
    50-->25;
    50-->75;
    25-->30;
    30-->27;
    30-->40;
    75-->90;
    75-->60;
    90-->85;
```
---
---
 # Balance node
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
Ex output array inorder traversal: [60 ,23 ,75 ,14 ,25 ,18 ,20 ] --> [14 ,18 ,20 ,23 ,25 ,60 ,75 ]

---
> code balance node (outside class):
```
header = balance_tree(inorder,header)
```
```
def con_balance(nodes,start,end):
    if start > end:
        return ""
    mid=(start+end)//2
    header = Node(nodes[mid])

    header.left = con_balance(nodes,start,mid-1)
    header.right = con_balance(nodes,mid+1,end)

    return header
```    
```    
def balance_tree(header):
    nodes = header.inorderTraversal(header) #inorder
    Len = len(nodes)

    return con_balance(nodes,0,Len-1)
```
* diagrams before balance odd node Ex:
```mermaid
graph TD;
    60-->23;
    60-->75;
    23-->14;
    23-->25;
    14-->18;
    18-->20;
```
> after balance  :
```mermaid
graph TD;
    23-->18;
    23-->60;
    18-->14;
    18-->20;
    60-->25;
    60-->75;
```
---
* diagrams before balance even node Ex:
```mermaid
graph TD;
    60-->23;
    60-->75;
    23-->14;
    23-->25;
    14-->18;
```
> after balance  :
```mermaid
graph TD;
    25-->18;
    25-->75;
    18-->14;
    18-->23;
    75-->60;
```
---
---
# Find maximum height, parent ,children ,leaves <br />
Ex. Node :<br />
   N = Node
```mermaid
graph TD;
    N1-->N2;
    N1-->N3;
    N2-->N4;
    N2-->N5;
    N3-->N6;
```
---
1.) maximum height :<br />
    LV = level
```mermaid
graph TD;
    N1(LV0)-->N2(LV1);
    N1(LV0)-->N3(LV1);
    N2(LV1)-->N4(LV2);
    N2(LV1)-->N5(LV2);
    N3(LV1)-->N6(LV2);
```
height = highest level + 1<br />
       = 2 + 1<br />
       = 3
       
---
2.) parent :<br />
 * nodethat containnextleft orright node<br />
 N = other Node<br />
 P = parent 
```mermaid
graph TD;
    N1(P1)-->N2(P2);
    N1(P1)-->N3(P3);
    N2(P2)-->N4(N);
    N2(P2)-->N5(N);
    N3(P3)-->N6(N);
```
---
3.) children :<br />
 * node that contain previous node<br />
 N = other Node<br />
 C = children
```mermaid
graph TD;
    N1(N)-->N2(C1);
    N1(N)-->N3(C2);
    N2(C1)-->N4(C3);
    N2(C1)-->N5(C4);
    N3(C2)-->N6(C5);
```
---
4.) leaves : <br />
 * node that does not contain next left or right node<br />
  N = other Node<br />
  L = leaves
 ```mermaid
graph TD;
    N1(N)-->N2(N);
    N1(N)-->N3(N);
    N2(N)-->N4(L1);
    N2(N)-->N5(L2);
    N3(N)-->N6(L3);
```
---
5.) sibling : <br />
 * node that has the same parent<br />
  N = other Node<br />
  S = sibling
 ```mermaid
graph TD;
    N1(N)-->N2(S1);
    N1(N)-->N3(S1);
    N2(S1)-->N4(S2);
    N2(S1)-->N5(S2);
    N3(S1)-->N6(N);
```
---
