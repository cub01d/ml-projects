# perceptron

Simple perceptron linear classifier to learn a random target function.

Source code in [`perceptron.py`](./perceptron.py). Jupyter notebook also included.

## Process
- Pick 2 random 2-d points. This is the decision boundary to be learned.
- Randomly generate N data points as training data.
- Label the N training data points.
- Initialize perceptron weights to zero.
- Adjust weights according to the perceptron learning algorithm until converged. 
- Repeat experiment over 1000 trials to note down statistics.


## Statistics
- Notes down on average how many iterations the algorithm takes to converge
- Estimates amount of disagreement between target function and learned boundary (final hypothesis)
    - Monte Carlo methods: generate test data and compare target function with our hypothesis

