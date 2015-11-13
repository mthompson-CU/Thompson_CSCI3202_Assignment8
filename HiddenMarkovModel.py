# Author: Matthew Thompson
# Date: 11/11/15
# Implements a Hidden Markov Model for use in Assignment 8

class HiddenMarkovModel():
	def __init__(self, states, observations):
		self.states = states
		self.observations = observations
		self.transitionProbabilities = {}
		self.emissionProbabilities = {}
		self.marginalProbabilities = {}

	def calculateTransitionProbabilites(self):
		# Add all states
		for state in self.states:
			if (not state in self.transitionProbabilities):
				self.transitionProbabilities[state] = {}

		# Count transitions
		for x in range(len(self.states) - 1):
			if (not self.states[x + 1] in self.transitionProbabilities[self.states[x]]):
				self.transitionProbabilities[self.states[x]][self.states[x + 1]] = 1
			else:
				self.transitionProbabilities[self.states[x]][self.states[x + 1]] += 1		
		
		# Normalize and smooth
		stateSum = 0.0
		for state in self.transitionProbabilities:
			for transitionState in self.transitionProbabilities[state]:
				stateSum += self.transitionProbabilities[state][transitionState]
			
			for transitionState in self.transitionProbabilities[state]:
				probability = float(self.transitionProbabilities[state][transitionState] + 1) / (stateSum + 27)
				self.transitionProbabilities[state][transitionState] = probability
			
			stateSum = 0.0

		# Output
		print 'Transition Probabilities'
		print '------------------------\n'

		for state in self.transitionProbabilities:
			for transitionState in self.transitionProbabilities[state]:
				print 'P(X(t+1) = ' + transitionState + '|X(t) = ' + state + '): ' + str(self.transitionProbabilities[state][transitionState])

	def calculateEmissionProbabilities(self):
		# Add all states
		for state in self.states:
			if (not state in self.emissionProbabilities):
				self.emissionProbabilities[state] = {}

		# Count observations
		for x in range(len(self.states)):
			if (not self.observations[x] in self.emissionProbabilities[self.states[x]]):
				self.emissionProbabilities[self.states[x]][self.observations[x]] = 1
			else:
				self.emissionProbabilities[self.states[x]][self.observations[x]] += 1

		# Normalize and smooth
		stateSum = 0.0
		for state in self.emissionProbabilities:
			for observation in self.emissionProbabilities[state]:
				stateSum += self.emissionProbabilities[state][observation]
			
			for observation in self.emissionProbabilities[state]:
				probability = float(self.emissionProbabilities[state][observation] + 1) / (stateSum + 27)
				self.emissionProbabilities[state][observation] = probability
			
			stateSum = 0.0

		# Output
		print '\nEmission Probabilities'
		print '----------------------\n'

		for state in self.emissionProbabilities:
			for observation in self.emissionProbabilities[state]:
				print 'P(E(t) = ' + observation + '|X(t) = ' + state + '): ' + str(self.emissionProbabilities[state][observation])

	def calculateMarginalProbabilities(self):
		# Add all states
		for state in self.states:
			if (not state in self.marginalProbabilities):
				self.marginalProbabilities[state] = 1
			else:
				self.marginalProbabilities[state] += 1

		# Normalize
		statesSum = 0.0
		for state in self.marginalProbabilities:
			statesSum += self.marginalProbabilities[state]

		for state in self.marginalProbabilities:
			self.marginalProbabilities[state] = float(self.marginalProbabilities[state]) / statesSum

		# Output
		print '\nMarginal Probabilities'
		print '----------------------\n'

		for state in self.marginalProbabilities:
			print 'P(X[0] = ' + state + '): ' + str(self.marginalProbabilities[state])

