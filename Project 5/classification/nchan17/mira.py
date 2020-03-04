# mira.py
# -------
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


# Mira implementation
import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        self.features = trainingData[0].keys() # this could be useful for your code later...

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    # function trainAndTune of MIRA classifier sets weights based on training data and Cgrid
    # it returns the weights that give us highest accuracy with validationData
    # implementation uses basic formulas of multi-class MIRA classifier to set weights
    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        """
        This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid,
        then store the weights that give the best accuracy on the validationData.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        representing a vector of values.
        """
        "*** YOUR CODE HERE ***"
                                       
        res = []
        best_acc = 0
        for c in Cgrid:
            curr_acc = 0
            tau = c
            for it in range(self.max_iterations):
                for i_data in range(len(trainingData)):
                    ith_train_data = trainingData[i_data] 
                    y_highest = self.classify([ith_train_data])[0]
                    y_true = trainingLabels[i_data]
                    
                    if y_highest != y_true:
                        weight = self.weights
                        try_tau = (1.0 + (weight[y_highest] - weight[y_true]) * ith_train_data) / (ith_train_data * ith_train_data * 2.0)
                        # try_tau /= ith_train_data * ith_train_data * 2.0
                        if try_tau < c: tau = try_tau
                        else: tau = c
                        bla = self.classify([trainingData[i_data] ])[0]
                        for j in trainingData[i_data] :
                            curr_multiplier = ith_train_data[j] * tau
                            self.weights[y_true][j] += curr_multiplier
                            self.weights[y_highest][j] -= curr_multiplier
                            
            pred_len = len(self.classify(validationData))
            for i in range(pred_len):
                if self.classify(validationData)[i] == validationLabels[i]:
                    curr_acc += 1
            curr_acc /= (pred_len * 1.0)
            if best_acc < curr_acc:
                res = self.weights
                best_acc = curr_acc
        self.weights = res  


    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


