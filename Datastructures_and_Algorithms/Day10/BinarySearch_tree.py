'''Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

checkBST has the following parameter(s):

root: a reference to the root node of a tree to test
Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.

Sample Input

image

Sample Output

Yes
Explanation

The tree in the diagram satisfies the ordering property for a Binary Search Tree, so we print Yes. in python
Hackerrank link: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root, prev=[None]):
    if root is None:
        return True

    if not isBST(root.left, prev):
        return False

    if prev[0] is not None and root.data <= prev[0].data:
        return False

    prev[0] = root

    return isBST(root.right, prev)


def checkBST(root):
    return isBST(root)
