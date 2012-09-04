# coding=utf-8
from utils import FifoList, AddOnceList, AddOnceFifoList
from models import SearchNode


def breadth_first_tree_search(problem):
    return _tree_search(problem, FifoList())


def depth_first_tree_search(problem):
    return _tree_search(problem, [])


def breadth_first_graph_search(problem):
    return _tree_search(problem, AddOnceFifoList())


def depth_first_graph_search(problem):
    return _tree_search(problem, AddOnceList())


def limited_depth_first_tree_search(problem, depth_limit):
    return _tree_search(problem, [], depth_limit=depth_limit)


def limited_depth_first_graph_search(problem, depth_limit):
    return _tree_search(problem, AddOnceList(), depth_limit=depth_limit)


def _tree_search(problem, fringe, depth_limit=None):
    fringe.append(SearchNode(state=problem.initial_state,
                             parent=None,
                             cost=0,
                             problem=problem,
                             depth=0))
    while fringe:
        node = fringe.pop()
        if node.has_goal_state():
            return node
        if depth_limit is None or node.depth < depth_limit:
            fringe.extend(node.expand())
    return None