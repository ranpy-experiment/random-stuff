"""
2196. Create Binary Tree From Descriptions
Difficulty: Medium
https://leetcode.com/problems/create-binary-tree-from-descriptions/

──────────────────────────────────────────────────

You are given a 2D integer array descriptions where descriptions[i] =
[parenti, childi, isLefti] indicates that parenti is the parent of
childi in a binary tree of unique values. Furthermore,

	• If isLefti == 1, then childi is the left child of parenti.

	• If isLefti == 0, then childi is the right child of parenti.

Construct the binary tree described by descriptions and return its
root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:

Input: descriptions =
[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no
parent.
The resulting binary tree is shown in the diagram.

Example 2:

Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no
parent.
The resulting binary tree is shown in the diagram.

 

Constraints:

	• 1 <= descriptions.length <= 10^4

	• descriptions[i].length == 3

	• 1 <= parenti, childi <= 10^5

	• 0 <= isLefti <= 1

	• The binary tree described by descriptions is valid.
"""

from typing import List, Optional, Dict, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Description:
	def __init__(self, description_list: List[int]):
		self.value = description_list[0]
		self.child = description_list[1]
		self.is_left = description_list[2]

	def left_child_value(self) -> Optional[int]:
		if self.is_left:
			return self.child
		return None
	
	def right_child_value(self) -> Optional[int]:
		if self.is_left:
			return None
		return self.child



class Solution:
	def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
		# basically, what I am thinking at the moment is that, maybe we can do something like this..
		# create an array representation of the tree, and then we can construct the treenode later
		# now, to create the array representation as well, it would have nice to have a sort of a map
		# because parent is going to be common, and we will need to see if this number exists in the tree or not
		# maybe we can keep a map of the value to treenode, that might be helpful

		node_cache: Dict[int, TreeNode] = {}
		parent_map: Dict[int, int] = {}

		for desc_raw in descriptions:
			desc: Description = Description(desc_raw)
			node:TreeNode = self.resolve_node(desc, node_cache)
			self.update_cache(node_cache, node)
			self.update_parent(node, parent_map)

		return self.find_parent(parent_map, node_cache)



	def resolve_node(self, desc: Description, node_cache: Dict[int, TreeNode]) -> TreeNode:
		left_child_value: Optional[int] = desc.left_child_value()
		if left_child_value:
			left_node: Optional[TreeNode] = node_cache.get(left_child_value, TreeNode(left_child_value))
		else:
			left_node = None
		
		right_child_value: Optional[int] = desc.right_child_value()
		if right_child_value: 
			right_node: Optional[TreeNode] = node_cache.get(right_child_value, TreeNode(right_child_value))
		else:
			right_node = None

		if desc.value in node_cache:
			root_node: TreeNode = node_cache.get(desc.value, TreeNode(desc.value))
			if left_node:
				root_node.left = left_node
			if right_node:
				root_node.right = right_node
		else:
			root_node = TreeNode(desc.value, left_node, right_node)
		return root_node

	def update_cache(self, node_cache: Dict[int, TreeNode], node: TreeNode) -> None:
		node_cache[node.val] = node
		if node.left:
			node_cache[node.left.val] = node.left
		if node.right:
			node_cache[node.right.val] = node.right

	def update_parent(self, node: TreeNode, parent_map: Dict[int, int]) -> None:
		if node.left:
			parent_map[node.left.val] = node.val
		if node.right:
			parent_map[node.right.val] = node.val

	def find_parent(self, parent_map: Dict[int, int], node_cache: Dict[int, TreeNode]) -> TreeNode:
		child_values: Set[int] = set(parent_map.keys())
		all_values: Set[int] = set(node_cache.keys())

		root_value_set: Set[int] = all_values - child_values
		if root_value_set is None or len(root_value_set) != 1:
			raise RuntimeError("I screwed up!! Try again. Found this: ", str(root_value_set))
		
		root_value: int = list(root_value_set)[0]
		root_node: Optional[TreeNode] = node_cache.get(root_value)
		if root_node is None:
			raise RuntimeError("No node with value: ", str(root_value))
		
		return root_node


if __name__ == "__main__":
	sol = Solution()
	sol.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
    