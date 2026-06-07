import pytest
from typing import Optional, List, Deque
from create_binary_tree_from_descriptions import Solution, TreeNode
from collections import deque

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    q: Deque[Optional[TreeNode]] = deque([root])
    out: List[Optional[int]] = []
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    # trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out

@pytest.mark.parametrize("input_args, expected", [
    ([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]], [50,20,80,15,17,19]),
    ([[1,2,1],[2,3,0],[3,4,1]], [1,2,None,None,3,4])
])
def test_example_cases(input_args: List[List[int]], expected: List[Optional[int]]):
    solution: Solution = Solution()
    response: Optional[TreeNode] = solution.createBinaryTree(input_args)

    assert tree_to_list(response) == expected

    

