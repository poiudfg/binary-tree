# Binary tree from python

________________________________________________________________________________________________________________________________________________________ <br />
- [x] Insertion a new node function in binary tree
- [x] Sorted bumber (Adding node)
- [x] Deletion a node function in binary tree
- [x] Balance node function in binary tree 
- [x] Find maximum height
- [x] Find parent
- [x] Find children
- [x] Find leaves
- [x] Find sibling
<br />
________________________________________________________________________________________________________________________________________________________ <br />
* Insertion a new node and Sorted bumber <br />
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
<br />
________________________________________________________________________________________________________________________________________________________ <br />
