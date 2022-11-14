import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    if not root:
        return []
    if not root.right and not root.left:
        return [str(root.val)]
    res = []
    if root.left:
        path_to_left = binary_tree_paths(root.left)
        res = [str(root.val) + "->" + path for path in path_to_left]

    if root.right:
        path_to_right = binary_tree_paths(root.right)
        res.extend([str(root.val) + "->" + path for path in path_to_right])

    return res


def test_given_the_root_of_a_binary_tree_return_all_root_to_leaf_paths_in_any_order():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    assert binary_tree_paths(root) == ["1->2->5", "1->3"]


def test_given_the_root_with_only_left_child_return_root_to_leaf_path():
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert binary_tree_paths(root) == ["1->2"]


def test_given_the_root_with_only_right_child_return_root_to_leaf_path():
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert binary_tree_paths(root) == ["1->2"]


@pytest.mark.parametrize("root, expected", [(1, "1"), (2, "2")])
def test_given_the_root_without_children_return_root_itself(root, expected):
    root = TreeNode(root)
    assert binary_tree_paths(root) == [expected]


def test_given_no_root_return_empty_list():
    assert binary_tree_paths(root=None) == []
