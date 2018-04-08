
class Node:
 
    # Constructor for creating a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
# Function for printing all the keys in the given range
# [r1..r2] 
def Print(root, r1, r2):
    
    if root is None:
        return

    #If root.value is greater than r1, then only we can get
    # keys in left subtree
    if r1 < root.value :
        Print(root.left, r1, r2)
 
    # If root's value lies in range, then prints root's value
    if r1 <= root.value and r2 >= root.value:
        print (root.value,)
 
    # If root.value is smaller than r2, then only we can get
    # keys in right subtree
    if r2 > root.value:
        Print(root.right, r1, r2)
 
# Inputs to test above function
# Taking user inouts for r1 and r2
print("-------Enter the Range------")
r1 = int(input("Enter r1 : "))
r2 = int(input("Enter r2 : "))


#The BST is created from the given input.
root = Node(19)
root.left = Node(7)
root.right = Node(43)
root.left.left = Node(3)
root.left.right = Node(11)
root.left.left.left = Node(2)
root.left.left.right = Node(5)
root.left.right.right = Node(17)
root.left.right.right.left = Node(13)

root.right.left = Node(23)
root.right.left.right = Node(37)
root.right.left.right.left = Node(29)
root.right.left.right.left.right = Node(31)
root.right.left.right.right = Node(41)
root.right.right = Node(47)
 
#Printing the results.

print("\nBST keys that lie between the %d and %d \n" % (r1,r2))
Print(root, r1, r2)
