import appJar
import pickle

from collect_data import getDatasetFromSentence

def test_sentence(classifier, sentence): 
    return classifier.classify(getDatasetFromSentence(sentence))

def press(btn):
	classifier = pickle.load(open("classifier.pickle", "rb"))
	res = test_sentence(classifier, gui.getTextArea('text'))
	if (res == 'pos'):
		cls = 'This is a positive comment'
		gui.setLabelBg('result', 'green')
	else:
		cls = 'This is a negative comment'
		gui.setLabelBg('result', 'red')
	gui.setLabel("result", "Classification result: " + cls)

gui = appJar.gui("Movie review classifier", "600x300")

gui.setBg("lightBlue")
gui.setFont(15)
gui.addLabel("label", "Enter text to classify")
gui.addTextArea("text")
gui.addButton("Classify", press)
gui.addLabel("result", "Classification result: ")
gui.setTextAreaFocus("text")

gui.go()