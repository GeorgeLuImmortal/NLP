# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator

def loadDataset(filename, k):
	with open(filename, 'rU') as csvfile:
	    lines = csv.reader(csvfile)
       
	    dataset = list(lines)
	    for x in range(len(dataset)):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
            random.shuffle(dataset)# shuffle dataset
	    size=len(dataset)/k
            part_k=[]
            for x in range(k):
                start=x*size
                end=len(dataset) if x==k-1 else (start+size)
                part_k.append(dataset[start:end])
            return part_k

def euclideanDistance(instance1, instance2, length):#return euclideanDistance
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)# get the distance between test and training
		distances.append((trainingSet[x], dist))
    
	distances.sort(key=operator.itemgetter(1))#sort by dist
	neighbors = []
	for x in range(k):# append K nearest neighbors 
		neighbors.append(distances[x][0])#get neighbors
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
		if testSet[x][-1] == predictions[x]:#test accuracy
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def setDatasets(dataSets, Index):
    trainingSet = []
    testSet = []
    for partIndex in range(len(dataSets)): # set test set and training set
        if partIndex == Index:
            testSet = dataSets[partIndex]
        else:
            trainingSet += dataSets[partIndex]
    return trainingSet, testSet

	
def main():
	# prepare data
        k=5
	trainingSet=[]
	testSet=[]
	part_k=loadDataset('F:/ucd/TextAnalysis/xLect6.Progs/xLect6.Progs/iris.csv', k)
        print(len(part_k))
        
        accuracy=[]
        for dataSetIndex in range(len(part_k)):
            predictions=[]
            trainingSet, testSet = setDatasets(part_k, dataSetIndex)
            for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet,testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
            accuracy.append(getAccuracy(testSet, predictions))
        print(accuracy)
        print(sum(accuracy)/k)

	
            
	
main()
