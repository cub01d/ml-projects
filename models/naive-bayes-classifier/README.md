# Naive Bayes Classifier

This project aims to classify movie reviews as either positive or negative.

The following files were provided:
- [`training.txt`](./training.txt): A compilation of 5000 total movie reviews, both positive and negative.
- [`testing.txt`](./testing.txt): Testing data with 500 movie reviews to validate accuracy of labels.

## Example movie review
```
I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge.	1
```

Each text file contains an entire movie review on one line, followed by a tab character and the label: `0` (negative) or `1` (positive).

## Running the program
Give NaiveBayesClassifier executable permissions:

	$ chmod +x NaiveBayesClassifier
and then run it with

	$ ./NaiveBayesClassifier training.txt testing.txt
    
## Model details
This movie review classifier implements a [bag of words model](https://en.wikipedia.org/wiki/Bag-of-words_model) to learn a vocabulary and the probabilities of each word being positive or negative.
The program will then label the reviews as positive or negative depending on the probability calculated with [Maximum Likelihood Estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation). For each review in `testing.txt`, it will output one label per line, and then calculate the training time, labeling time, training accuracy, and testing accuracy.

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
