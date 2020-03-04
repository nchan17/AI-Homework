# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    # Evaluation Function for Reflex Agent
    # Takes current and successor states and returns number. 
    # Higher number means preferrable state.
    # To implement function we calculate minimum distance from pacman to ghosts and food.
    # While finding distances we use manhatten distance.
    # The closer ghost is the less score should be
    # The closer food is the higher score should be
    # But if ghost is very close the result is very undisirable
    # Final result is calculated based on this concepts
    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood().asList()
        newGhostStates = successorGameState.getGhostStates()
        newGhostPositions = successorGameState.getGhostPositions()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        closestGhostDist = float("inf")
        closestFoodDist = float("inf")
        veryBad = float("-inf")

        for dot in newFood:
          dist = manhattanDistance(newPos, dot)
          if(dist < closestFoodDist):
            closestFoodDist = dist

        for ghost in newGhostPositions:
          dist = manhattanDistance(newPos, ghost)
          if(dist < closestGhostDist):
            closestGhostDist = dist

        if(closestGhostDist < 2): 
          return veryBad
          
        return 1.0/closestFoodDist - 1.0/closestGhostDist + successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    # getAction calculates what next action should be in MinimaxAgent.
    # As pacman is the one that startes the game, the first call should be maximizer.
    # Algorithm compares all the values certain actions will get us and returnes the action with most score.
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
       
        # Takes gameState, depth and agent index as arguments
        # "value" is helper function for recursion, that directs whether value should be minimized or maximized 
        # If agent is ghost returns Minimal Value
        # if agent is pacman returns Maximal Value
        # If state is terminal returnes state's utility
        def value(self, gameState, depth, index):
          index = index + 1
          if index >= gameState.getNumAgents():
            index -= (index / gameState.getNumAgents()) * gameState.getNumAgents()
          if gameState.isWin() or gameState.isLose() or (index == 0 and depth == self.depth):
            currValue = self.evaluationFunction(gameState)
          elif(index == 0):
            currValue = max_value(gameState, self, depth + 1, index)
          else:
            currValue = min_value(gameState, self, depth, index)
          return currValue

        # min_value is a minimizer that tries to get minimal score possible,
        # it represents ghosts side of algorithm
        # Takes game state, depth and agent index and returnes minimal value
        # A minimizer also consideres what moves will oponent make.
        # Depth is current depth in the game tree.
        def min_value(gameState, self, depth, index):
          v = float("inf")
          for action in gameState.getLegalActions(index):
            v = min(v, value(self, gameState.generateSuccessor(index, action), depth, index))
          return v

        # max_value is a maximizer that tries to get maximal score possible,
        # it represents pacmans side of algorithm
        # Takes game state, depth and agent index and returnes maximal value
        # A maximizer also consideres what moves will oponent make.
        # Depth is current depth in the game tree.
        def max_value(gameState, self, depth, index):
          v = float("-inf")
          for action in gameState.getLegalActions(index):
            v = max(v, value(self, gameState.generateSuccessor(index, action), depth, index))
          return v

        v = float("-inf") 
        act = Directions.STOP
        for action in gameState.getLegalActions(0):
          currValue = value(self, gameState.generateSuccessor(0, action), 1, 0)
          if currValue > v :
            v = currValue
            act = action
        return act



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    # getAction calculates what next action should be in AlphaBetaAgent.
    # As pacman is the one that startes the game, the first call should be maximizer.
    # Algorithm compares all the values certain actions will get us and returnes the action with most score.
    # Alpha is the best value that the maximizer currently can guarantee at that level or above, as default it's -infinity
    # Beta is the best value that the minimizer currently can guarantee at that level or above, as default it's infinity
    # Depth is current depth in game tree.
    # While calculating it removes all the nodes that are not effecting final decision and are making algorithm slow.
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # Takes gameState, depth, agent index, alpha and beta  as arguments
        # "value" is helper function for recursion, that directs whether value should be minimized or maximized 
        # If agent is ghost returns Minimal Value
        # if agent is pacman returns Maximal Value
        # If state is terminal returnes state's utility
        def value(self, gameState, depth, index, alpha, beta):
          index = index + 1
          if index >= gameState.getNumAgents():
            index -= (index / gameState.getNumAgents()) * gameState.getNumAgents()
          if gameState.isWin() or gameState.isLose() or (index == 0 and depth == self.depth):
            currValue = self.evaluationFunction(gameState)
          elif(index == 0):
            currValue = max_value(gameState, self, depth + 1, index, alpha, beta)
          else:
            currValue = min_value(gameState, self, depth, index, alpha, beta)
          return currValue

        # min_value is a minimizer that tries to get minimal score possible,
        # it represents ghosts side of algorithm
        # Takes game state, depth and agent index and returnes minimal value
        # A minimizer also consideres what moves will oponent make.
        # while calculating it removes all the nodes that are not effecting final decision.
        # Depth is current depth in the game tree.
        # Min player updates only beta.
        def min_value(gameState, self, depth, index, alpha, beta):
          v = float("inf")
          for action in gameState.getLegalActions(index):
            v = min(v, value(self,gameState.generateSuccessor(index, action), depth, index, alpha, beta))
            if v < alpha:  return v
            else: beta = min (beta, v)
          return v

        # max_value is a maximizer that tries to get maximal score possible,
        # it represents pacmans side of algorithm
        # Takes game state, depth and agent index and returnes maximal value
        # while calculating it removes all the nodes that are not effecting final decision.
        # A maximizer also consideres what moves will oponent make.
        # Depth is current depth in the game tree.
        # Max player updates only alpha
        def max_value(gameState, self, depth, index, alpha, beta):
          v = float("-inf")
          for action in gameState.getLegalActions(index):
            v = max(v, value(self, gameState.generateSuccessor(index, action), depth, index, alpha, beta))
            if v > beta : return v
            else: alpha = max(alpha, v)
          return v

        v = float("-inf")
        act = Directions.STOP 
        alpha = float("-inf") 
        beta = float("inf") 
        for action in gameState.getLegalActions(0):
          currValue = value(self, gameState.generateSuccessor(0, action), 1, 0, alpha, beta)
          if currValue > v :
            v = currValue
            act = action
            alpha = max(alpha, v)
        return act
        
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    # getAction calculates what next action should be in ExpectimaxAgent.
    # As pacman is the one that startes the game, the first call should be maximizer.
    # Algorithm compares all the values certain actions will get us and returnes the action with most score.
    # It consideres that oponents (ghosts) are possibly making random moves.
    # Depth is depth of game tree.
    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        # Takes gameState, depth and agent index as arguments
        # "value" is helper function for recursion, that directs whether value should be minimized or maximized 
        # If agent is ghost returns Minimal Expected Value
        # if agent is pacman returns Maximal Value
        # If state is terminal returnes state's utility
        def value(self, gameState, depth, index):
          index = index + 1
          if index >= gameState.getNumAgents():
            index -= (index / gameState.getNumAgents()) * gameState.getNumAgents()
          if gameState.isWin() or gameState.isLose() or (index == 0 and depth == self.depth):
            currValue = self.evaluationFunction(gameState)
          elif(index == 0):
            currValue = max_value(gameState, self, depth + 1, index)
          else:
            currValue = exp_value(gameState, self, depth, index)
          return currValue

        # max_value is a maximizer that tries to get maximal score possible,
        # it represents pacmans side of algorithm
        # Takes game state, depth and agent index and returnes maximal value
        # A maximizer also consideres what moves will oponent make.
        # Depth is current depth in the game tree.
        def max_value(gameState, self, depth, index):
          v = float("-inf")
          for action in gameState.getLegalActions(index):
            v = max(v, value(self, gameState.generateSuccessor(index, action), depth, index))
          return v

        # exp_value calculates expected utilities.
        # it represents ghosts side of algorithm, since ghosts are playing randomly, each action has same probability.
        # Takes game state, depth and agent index and returnes expected value
        # It also consideres what moves will oponent make.
        # Depth is current depth in the game tree. 
        def exp_value(gameState, self, depth, index):
          v = 0
          size = len(gameState.getLegalActions(index))
          for action in gameState.getLegalActions(index):
            p = 1.0 / size
            v += p * value(self, gameState.generateSuccessor(index, action), depth, index)
          return v
          
        v = float("-inf") 
        act = Directions.STOP
        for action in gameState.getLegalActions(0):
          currValue = value(self, gameState.generateSuccessor(0, action), 1, 0)
          if currValue > v :
            v = currValue
            act = action
        return act


# betterEvaluationFunction is evaluation function that Takes current state and returns number. 
# Higher number means preferrable state.
# To implement function we calculate minimum distance from pacman to ghosts and food.
# While finding distances we use manhatten distance.
# The closer ghost is the less score should be
# The closer food is the higher score should be, if there are no foods remaining the result is very disirable
# But if ghost is very close the result is very undisirable
# If Pacman has eaten power pellet that is still active, we can stop worrying about ghosts and assume they are far away
# Final result is calculated based on this concepts
def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    def findMyManhattanDistance(one, two):
      return abs(one[0] - two[0]) + abs(one[1] - two[1])

    pos = currentGameState.getPacmanPosition()		
    food = currentGameState.getFood().asList()				
    ghostStates = currentGameState.getGhostStates()
    ghostPositions = currentGameState.getGhostPositions()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
        
    closestFoodDist = float("inf")
    closestGhostDist = float("inf")
    veryBad = float("-inf")

    for ghost in ghostPositions:
      dist = findMyManhattanDistance(pos, ghost)
      if(dist < closestGhostDist):
        closestGhostDist = dist
    if(closestGhostDist < 2): return veryBad
    elif scaredTimes[0] >= 1: resGhost = (-1.0 / closestGhostDist) * pow(0.1, 6)
    else: resGhost = -1.0 / closestGhostDist

    counter = 0
    for dot in food:
      counter += 1
      dist = findMyManhattanDistance(pos, dot)
      if(dist < closestFoodDist):
        closestFoodDist = dist   
    if counter == 0: resFood = pow(10, 6)
    else: resFood = 1.0 / closestFoodDist

    return resFood + resGhost + currentGameState.getScore()

# Abbreviation
better = betterEvaluationFunction

