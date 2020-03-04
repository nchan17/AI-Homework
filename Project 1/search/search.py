# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


    # This implementation of DFS uses Stack as main memorisation tool.
    # It is useful because, stack pops last pushed element.
    # So we know for sure that stack each time will pop last element we added to a fringe.
    # implementation : At first we push starting point and path we had to take to get there ( = 0)
    # in loop until we explore all nodes we pop node and push each of Successors of current node
    # with new path (which is path of currNode + successor node).
    # loop will finish when we reach the goal or explore all nodes.
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    seen = []
    pathMemo = util.Stack()
    memo = util.Stack()
    memo.push(problem.getStartState())
    pathMemo.push([])
    while not memo.isEmpty():
        currSt = memo.pop()
        path = pathMemo.pop()
        if problem.isGoalState(currSt):
            return path
        elif currSt not in seen:
            seen.append(currSt)
            for successor in problem.getSuccessors(currSt):
                memo.push(successor[0])
                pathMemo.push(path + [successor[1]])

    return []
    util.raiseNotDefined()


    # This implementation of BFS uses Queue as main memorisation tool.
    # It is useful because, Queue pops first pushed element.
    # So we know for sure that Queue each time will pop first element we added to a fringe.
    # implementation : At first we push starting point and path we had to take to get there ( = 0)
    # in loop until we explore all nodes we pop node and push each of Successors of current node
    # with new path (which is path of currNode + successor node)
    # loop will finish when we reach the goal or explore all nodes.
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    seen = []
    pathMemo = util.Queue()
    memo = util.Queue()
    memo.push(problem.getStartState())
    pathMemo.push([])
    while not memo.isEmpty():
        currSt = memo.pop()
        path = pathMemo.pop()
        if problem.isGoalState(currSt):
            return path
        elif currSt not in seen:
            seen.append(currSt)
            for successor in problem.getSuccessors(currSt):
                memo.push(successor[0])
                pathMemo.push(path + [successor[1]])

    return []
    util.raiseNotDefined()


    # This implementation of uniformCostSearch uses PriorityQueue as main memorisation tool.
    # It is useful because, PriorityQueue pops lowest-priority element from queue.
    # So we know for sure that PriorityQueue each time will pop lowest-priority element we added to a fringe.
    # Algorithm will work correctly if we make priority same as cost.
    # implementation : At first we push starting point and path we had to take to get there ( = 0), as well as cost ( = 0)
    # in loop until we explore all nodes we pop node and push each of Successors of current node
    # with new path (which is path of currNode + successor node) 
    # and new cost (which is cost to get to currNode + cost to get from currNode to successor node)
    # loop will finish when we reach the goal or explore all nodes.
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    seen = []
    pathMemo = util.PriorityQueue()
    memo = util.PriorityQueue()
    costMemo = util.PriorityQueue()
    memo.push(problem.getStartState(), 0)
    pathMemo.push([], 0)
    costMemo.push(0, 0)
    while not memo.isEmpty():
        currSt = memo.pop()
        path = pathMemo.pop()
        cost = costMemo.pop()
        if problem.isGoalState(currSt):
            return path
        elif currSt not in seen:
            seen.append(currSt)
            for successor in problem.getSuccessors(currSt):
                newCost = successor[2] + cost
                memo.push(successor[0], newCost)
                costMemo.push(newCost, newCost)
                pathMemo.push(path + [successor[1]], newCost)

    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# This implementation of aStarSearch uses PriorityQueue as main memorisation tool.
# It is useful because, PriorityQueue pops lowest-priority element from queue.
# So we know for sure that PriorityQueue each time will pop lowest-priority element we added to a fringe.
# Algorithm will work correctly if we make priority same as cost + heuristics.
# implementation : At first we push starting point and path we had to take to get there ( = 0), as well as cost ( = 0)
# in loop until we explore all nodes we pop node and push each of Successors of current node
# with new path (which is path of currNode + successor node) 
# and new cost (which is cost to get to currNode + cost to get from currNode to successor node)
# and finally with priority of new cost + heuristic
# loop will finish when we reach the goal or explore all nodes.
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    seen = []
    pathMemo = util.PriorityQueue()
    memo = util.PriorityQueue()
    costMemo = util.PriorityQueue()
    memo.push(problem.getStartState(), 0)
    pathMemo.push([], 0)
    costMemo.push(0, 0)
    while not memo.isEmpty():
        currSt = memo.pop()
        path = pathMemo.pop()
        cost = costMemo.pop()
        if problem.isGoalState(currSt):
            return path
        elif currSt not in seen:
            seen.append(currSt)
            for successor in problem.getSuccessors(currSt):
                newCost = successor[2] + cost
                heurist = newCost + heuristic(successor[0], problem)
                memo.push(successor[0], heurist)
                costMemo.push(newCost, heurist)
                pathMemo.push(path + [successor[1]], heurist)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
