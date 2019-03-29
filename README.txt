Data for this project is taken fro IMDB website. (For all other information about data there is README - data file where it also says wherethe dta is taken from.) 

There are three files with code: 

collect_data.py - In this file all necessary data preparations are performed - tokenizing it, detecting stemming words, stop words, do feature extraction, lemmatization, finding synonyms, removing duplicates. After this all tokens are stored in array and classified into positive or negative.  

train_data.py - Main file with the performing of training itself. All necessary libraries and classifiers are imported, training data performed and all of that together with results of accuracy of algorithms, which are in percentages, is shown in GUI.

gui.py - Graphical User interface for entering text on which sentiment analysis should be performed based on last saved training classifier.
