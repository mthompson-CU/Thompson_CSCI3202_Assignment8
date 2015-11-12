# Author: Matthew Thompson
# Date: 11/11/15
# Implements a Hidden Markov Model for use in Assignment 8

class HiddenMarkovModel():
	def __init__(self, states, observations):
		self.states = states
		self.observations = observations
		self.transitionProbabilities = {}
		self.emissionProbabilities = {}

	def calculateTransitionProbabilites (self):
		for state in self.states:
			if (not state in self.transitionProbabilities):
				self.transitionProbabilities[state] = {}

		for x in range(len(self.states) - 1):
			if (not self.states[x + 1] in self.transitionProbabilities[self.states[x]]):
				self.transitionProbabilities[self.states[x]][self.states[x + 1]] = 1
			else:
				self.transitionProbabilities[self.states[x]][self.states[x + 1]] += 1		
		
		stateSum = 0.0
		for state in self.transitionProbabilities:
			for transitionState in self.transitionProbabilities[state]:
				stateSum += self.transitionProbabilities[state][transitionState]
			
			for transitionState in self.transitionProbabilities[state]:
				probability = float(self.transitionProbabilities[state][transitionState]) / stateSum
				self.transitionProbabilities[state][transitionState] = probability
			
			stateSum = 0.0

		print 'Transition Probabilities'
		print '------------------------'

		for state in self.transitionProbabilities:
			for transitionState in self.transitionProbabilities[state]:
				print 'P(t+1 = ' + transitionState + '|t = ' + state + '): ' + str(self.transitionProbabilities[state][transitionState])



		# print self.transitionProbabilities	