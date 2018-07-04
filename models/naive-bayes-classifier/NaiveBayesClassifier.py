import sys
import string
import re
import time

def plain(s):
    return s.translate(string.maketrans("",""), string.punctuation).lower()

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, ' ', raw_html)
	return cleantext

bag = {}		# "word_i":[word counts in bag, word counts in +, p(w|+), p(w|-)]
docs = [0, 0]	# [total # reviews, # positive reviews]
total = [0,0,0]	# [total # words in vocabulary, total # words in positive reviews, total # in negative]
ppos = 0		# P(+) = 1 - p(-) 
k = 0.0
accuracy = [0,0]# [correct, incorrect]

def train(filename):
	global bag
	global docs
	global total
	global ppos
	global k  

	starttime = time.time()
	# read training data and create bag of words
	f = open(filename, "r")
	for line in f:
		docs[0] += 1
		clean = plain(cleanhtml(line))
		# each word in review
		for word in clean.split()[:-1]:
			if len(word) <= 4:
				continue
			# if word is not in bag, add it
			if word.lower() not in bag:
				bag[word.lower()] = [1, 0, 0, 0]
			else:
				bag[word.lower()][0] += 1

			if int(line[-2]):
				bag[word.lower()][1] += 1

		#if it is a word in a positive review, increase # positive words
		if int(line[-2]):
			docs[1] += 1
		total[0] += 1
		# update word counts
		if int(line[-2]):
			total[1] += 1
		else:
			total[2] += 1
	f.close()

	# calculate probabilities
	ppos = (docs[1] + k) / (docs[0] + k*2)
	# calculate P(word|+), p(word|-)

	for word in bag:
		bag[word][2] = (bag[word][1] + k) / (total[1] + k*len(bag))
		bag[word][3] = (bag[word][0] - bag[word][1] + k) / (total[2] + k*len(bag))

	# return time it takes to run
	return time.time() - starttime

def label(filename, printout):
	global ppos
	global accuracy

	starttime = time.time()
	f = open(filename)
	for line in f:
		doc = plain(cleanhtml(line))
		# classify each review on probabilities of each word
		positive = ppos
		negative = 1 - ppos
		for word in doc.split()[:-1]:
			if word in bag:
				positive *= bag[word][2]
				negative *= bag[word][3]
			else:
				positive *= (k / (total[1] + k*len(bag)) )
				negative *= (k / (total[2] + k*len(bag)) )
		if positive > negative:
			#correct
			if printout:
				print 1
			if int(line[-2]):
				accuracy[0] += 1
			else:
				accuracy[1] += 1
		else:
			if printout:
				print 0
			if not int(line[-2]):
				accuracy[0] += 1
			else:
				accuracy[1] += 1
	f.close()
	return time.time() - starttime

#./NaiveBayesClassifier training.txt testing.txt
# use training to generate all probabilities
training = train(sys.argv[1])
ltraining = label(sys.argv[1], False)
acctrain = accuracy[0]*1.0/(accuracy[0] + accuracy[1])
ltesting = label(sys.argv[2], True)
acctest = accuracy[0]*1.0/(accuracy[0] + accuracy[1])
print "{} seconds (training)".format(int(round(training)))
print "{} seconds (labeling)".format(int(round(ltraining + ltesting)))
print "{} (training)".format(acctrain)
print "{} (testing)".format(acctest)

import collections
toppos = {}
topneg = {}
topposp = {}
topnegp = {}
topwords = {}

for word in bag:
	topposp[word] = bag[word][2]
	topnegp[word] = bag[word][3]
	topwords[word] = bag[word][0]
	toppos[word] = bag[word][1]
	topneg[word] = bag[word][0]-bag[word][1]
pp = collections.Counter(topposp)
print pp.most_common(10)
#top 10 negative features
np = collections.Counter(topnegp)
print np.most_common(10)
#top 10 features
n = collections.Counter(topneg)
print n.most_common(10)
p = collections.Counter(toppos)
print p.most_common(10)
f = collections.Counter(topwords)
print f.most_common(10)
