# Part-Of-Speech-Tagger

In this assignment we will write a Hidden Markov Model part-of-speech tagger for Italian, Japanese, and a surprise language. The training data are provided tokenized and tagged; the test data will be provided tokenized, and tagger will add the tags. 

# Data
A set of training and development data is available as a compressed ZIP archive. The uncompressed archive will have the following files:

Two files (one Italian, one Japanese) with tagged training data in the word/TAG format, with words separated by spaces and each sentence on a new line.
Two files (one Italian, one Japanese) with untagged development data, with words separated by spaces and each sentence on a new line.
Two files (one Italian, one Japanese) with tagged development data in the word/TAG format, with words separated by spaces and each sentence on a new line, to serve as an answer key.

# Programs
There are two  programs in Python 3: hmmlearn.py will learn a hidden Markov model from the training data, and hmmdecode.py will use the model to tag new data.

The learning program will be invoked in the following way:

> python hmmlearn.py /path/to/input

The argument is a single file containing the training data; the program will learn a hidden Markov model, and write the model parameters to a file called hmmmodel.txt.

> python hmmdecode.py /path/to/input

The argument is a single file containing the test data; the program will read the parameters of a hidden Markov model from the file hmmmodel.txt, tag each word in the test data, and write the results to a text file called hmmoutput.txt in the same format as the training data.


