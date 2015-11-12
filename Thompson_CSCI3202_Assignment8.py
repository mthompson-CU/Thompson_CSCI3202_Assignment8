# Author: Matthew Thompson
# Date: 11/11/15
# Assignment 8

import sys
import HiddenMarkovModel

def importFile(fileName):
	textFile = open(fileName, 'rb')
	states = []
	observations = []
	for line in textFile:
		strippedLine = line.strip('\n')
		lineValues = strippedLine.split(' ')
		states.append(lineValues[0])
		observations.append(lineValues[1])

	return states, observations

def main (argv):
	states, observations = importFile(argv[1])
	hmm = HiddenMarkovModel.HiddenMarkovModel(states, observations)
	hmm.calculateTransitionProbabilites()

	return

if __name__ == '__main__':
	main(sys.argv)