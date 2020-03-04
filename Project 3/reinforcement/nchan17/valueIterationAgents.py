# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    # Given number of iterations, discount and mdp,
    # Function iteratively aproximates the values using dynamic programming,
    # updates values based of the best next state,
    # fills values list with k-step estimates of the optimal values
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for itr in range(self.iterations):
            currList = {}
            stateList = self.mdp.getStates()
            for st in stateList:
                if not self.mdp.isTerminal(st):
                    currList[st] = self.computeQValueFromValues(st, self.computeActionFromValues(st))
                else: 
                    currList[st] = self.values[st]

            self.values = currList

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    # returns Q-Value for certain action from state.
    # It iterates over Transition states and sums up Q-Value using MDP formula:
    # Q(s, a) = sumof (T(s,a,s') * [R(s,a,s') + gamma * V(s')])
    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        transList = self.mdp.getTransitionStatesAndProbs(state, action)
        gamma = self.discount
        QVal = 0
        for trans in transList:
            nextS = trans[0]
            T = trans[1]
            QVal += T * (self.mdp.getReward(state, action, nextS) + gamma * self.values[nextS])
        return QVal

    # Given state of the world, returns best posssible action.
    # Iterates over all possible legal actions and comuptes Q-value for each of them.
    # In the end returns the action which gave us the maximum Q-value out of all of them.
    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        maxVal = float('-inf')
        maxAct = None
        actionsList = self.mdp.getPossibleActions(state)
        for currAct in actionsList:
            currVal = self.computeQValueFromValues(state, currAct)
            if currVal > maxVal:
                maxVal = currVal
                maxAct = currAct
        return maxAct

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
