# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

# We want for policy to cause agent to cross the bridge
# To get the result we want, we should change answerNoise to 0, 
# or other very small number (preferrebly less then 0.01) 
# so that there's very slim risk of falling over the bridge unintended.
# That way policy will guide us over the bridge without worring about agent not following directions.
def question2():
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

# The optimal policy prefers the close exit (+1), risking the cliff (-10).
# There is minimum 4 moves from +1 to +10, so for our agent to exit on +1, each move
# should cost them nearly more then 10/4
# It also should be big enough that agent prefers to risk the cliff since it's the short way
# but if we make cost too big agent will prefer to exit on -10 right away.
# Let's leave answerDiscount and answerNoise same as previous question, 
# since it's easyer to calculate policy if agent never ends up in an unintended successor state.
# answerLivingReward should be roughly between -3.8 and -5.6
def question3a():
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = -4.7
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# The optimal policy prefers the close exit (+1), but avoiding the cliff (-10)
# There is minimum 4 moves from +1 to +10, so for our agent to exit on +1, each move
# should cost them nearly more then 10/4, if answerNoice is 0,
# But since cost should be small enough that agent prefers to go with long way
# it becomes hard to find such value. 
# answerNoise can not be zero and answerDiscount can not be such a big number because of reasons given above.
# So we should change answerDiscount and answerNoise to some small nonzero values.
def question3b():
    answerDiscount = 0.2
    answerNoise = 0.2
    answerLivingReward = 0.2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# The optimal policy prefers the distant exit (+10), risking the cliff (-10)
# There is minimum 4 moves from +1 to +10, so for our agent to exit on +1, each move
# should cost them nearly less then 10/4, if answerNoice is 0,
# answerLivingReward can not be more then 1, so that agent doesn't prefer to go the long way.
# So answerLivingReward is roughly between -2.5 and 0.9
# question 3a will be useful helper, since both are risking the cliff
def question3c():
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = -0.8
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# The optimal policy prefers the distant exit (+10), avoiding the cliff (-10)
# There is minimum 4 moves from +1 to +10, so for our agent to exit on +1, each move
# should cost them nearly less then 10/4, if answerNoice is 0,
# But since cost should be small enough that agent prefers to go with long way
# it becomes harder to find such value. 
# answerNoise can not be zero and answerDiscount because of reasons given above.
# So we should change answerLivingReward and answerNoise to some small nonzero values.
# question 3b(avoiding the cliff) and 3c(distant exit) will be useful helper
def question3d():
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# The optimal policy prefers to void both exits and the cliff (so an episode should never terminate)
# answerNoise and answerDiscount can be any number as long as answerLivingReward is big enough that 
# agent never wants to leave the game.
def question3e():
    answerDiscount = 0
    answerNoise = 0
    answerLivingReward = 10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# It's impossible to choose such epsilone and learning rate to give us the result we want.
# 50 itaretions is not enough for q-learning agent to come up with optimal policy,
# it might be enough but it's not highly likely.
def question6():
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
