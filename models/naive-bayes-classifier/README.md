# naive-bayes-classifier: Naive Bayes Classifier for movie reviews written in Python

This is a simple Naive Bayes Classifier for classifying movie reviews as positive or negative, written in Python2.7. This project was done for CS165A: Artificial Intelligence at UCSB. We were given training data and testing data for training our AI to label movie reviews as positive or negative. This implementation was very basic. I did not use word stemming methods. For each word, I used [additive smoothing](https://en.wikipedia.org/wiki/Additive_smoothing) to help calculate the probabilities. 

The following files were provided:
- [`training.txt`](./training.txt): Training data for our AI to calculate probabilities of words being positive or negative.
- [`testing.txt`](./testing.txt): Testing data to test accuracy of labels.

## Format of text files
```
I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge. 1
```

Each text file contains an entire movie review on one line, with a tab followed by either a `0` or a `1` depending on whether the review was negative or positive.

## Running program format
Give NaiveBayesClassifier executable permissions:

	chmod +x NaiveBayesClassifier
and then run it with

	./NaiveBayesClassifier training.txt testing.txt
    
The program will read in `training.txt` and create a [bag of words model](https://en.wikipedia.org/wiki/Bag-of-words_model). The program will then label the reviews in `testing.txt` as positive or negative depending on the probability calculated with [Maximum Likelihood Estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation). For each review in `testing.txt`, it will output one label per line, and then calculate some stats.

You may want to change the smoothing parameter `k` in [`NaiveBayesClassifier.py`](./NaiveBayesClassifier.py) for different results.

## Sample Output
```
...
0
0
0
0
1
0
0
0
1 seconds (training)
1 seconds (labeling)
0.5 (training)
0.499454545455 (testing)
```
