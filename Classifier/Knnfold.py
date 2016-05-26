from sklearn import cross_validation
import csv
import numpy as np
from sklearn.cross_validation import KFold
import math
import operator
import numpy

    
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	k=20
	accuracys=[]
	
	with open('F:/ucd/TextAnalysis/xLect6.Progs/xLect6.Progs/iris.csv','rU') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
        X = np.array(dataset)
        kf = cross_validation.KFold(len(dataset), n_folds=5, shuffle=False) #seperate dataset to 5 parts,1 for testing, the rest for training
        for train_index, test_index in kf:                                   
            predictions=[]
            print("TRAIN:", train_index, "TEST:", test_index)
            trainingSet, testSet = X[train_index], X[test_index]
            for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	    accuracys.append(getAccuracy(testSet, predictions))
	    
	print(accuracys)
	print(numpy.mean(accuracys))
	
	

	
main()