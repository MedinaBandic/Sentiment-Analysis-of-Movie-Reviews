from nltk import word_tokenize, PorterStemmer
from os import listdir
from os.path import isfile, join
import pickle

def getFilesInFolder(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def getStemmedWords(sentence):
    words = word_tokenize(sentence)
    stemmer = PorterStemmer()
    stemmed_words = map(lambda word: stemmer.stem(word).lower(), words)
    #we use set in order to remove duplicates
    return set(stemmed_words)

def getStemmedWordsFromFile(fname):
    f = open(fname, "r", encoding="utf8")
    words = getStemmedWords(f.read())
    f.close()
    return words

def getDataset(words, classification):
    #here we should do feature extraction, filtering out stop words, etc
    #and prepare data for training model
    ret = {}
    for word in words:
        # right now we set all the words to true, meaning we will train
        # our model for all words. If we dont want to train on all words
        # we simply set particular word to false (probably using frequency
        # analysis)
        ret[word] = True
    return (ret, classification)

def getDatasetFromSentence(sentence):
    return getDataset(getStemmedWords(sentence), 'x')[0]

def getDatasetFromFile(fname, classification):
    return getDataset(getStemmedWords(fname), classification)

def getAllDatasetsFromFolder(path):
    datasets = []
    for fname in getFilesInFolder(path + '/pos'):
        if fname != None:
            fpath = path + '/pos/' + fname
            print(fpath)
            datasets.append(getDataset(getStemmedWords(fpath), 'pos'))
    for fname in getFilesInFolder(path + '/neg'):
        if fname != None:
            fpath = path + '/neg/' + fname
            print(fpath)
            datasets.append(getDataset(getStemmedWords(fpath), 'neg'))
    return datasets

if __name__ == '__main__':
    trainDataset = getAllDatasetsFromFolder("aclImdb/train")
    testDataset = getAllDatasetsFromFolder("aclImdb/test")
    print("Dumping ...")
    trainFile = open("trainDataset.pickle", "wb")
    testFile = open("testDataset.pickle", "wb")
    pickle.dump(trainDataset, trainFile)
    pickle.dump(testDataset, testFile)
    trainFile.close()
    testFile.close()
