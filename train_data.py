import pickle
import appJar

trainFile = open("trainDataset.pickle", "rb")
testFile = open("testDataset.pickle", "rb")
trainDataset = pickle.load(trainFile)
testDataset = pickle.load(testFile)
trainFile.close()
testFile.close()

from nltk.classify.scikitlearn import SklearnClassifier
import nltk.classify
import math
import random
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import numpy as np

from collect_data import getDatasetFromSentence

classifiers = [LogisticRegression, SGDClassifier, SVC, LinearSVC, NuSVC, MultinomialNB, BernoulliNB]

trainings = 0
def trainPressed(btn):
	global trainings
	selected = gui.getOptionBox("Algorithm")
	for cls in classifiers:
		if cls.__name__ == selected:
			perc = train(cls)
			gui.addLabel("training" + str(trainings), selected + " finished with precision: " + str(perc))
			trainings += 1

def train(cls):
	classifier = SklearnClassifier(cls())
	classifier.train(trainDataset)
	f = open("classifier.pickle", "wb")
	pickle.dump(classifier, f)
	f.close()
	return nltk.classify.accuracy(classifier, testDataset) * 100.0
	

gui = appJar.gui("Movie review trainer")
gui.setBg("lightBlue")
gui.setFont(15)
gui.addLabelOptionBox("Algorithm", map(lambda c: c.__name__, classifiers))
gui.addButton("Train", trainPressed)
gui.go()
