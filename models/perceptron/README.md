# perceptron

Perceptron linear classifier that learns a random target function.

Source code in [`perceptron.py`](./perceptron.py). Jupyter notebook also included.

## Process
### Problem creation step
- Connect 2 random 2-d points. This is the decision boundary (target function) to be learned.
- Randomly generate N data points as training data.
- Label the N training data points according to the target function.
### Learning step 
- Initialize perceptron weights to zero (initial hypothesis).
- Adjust weights according to the perceptron learning algorithm until converged
(final hypothesis). 
- Repeat experiment over 1000 trials to gather perceptron performance statistics.


## Performance statistics of interest
- Average number of iterations the perceptron takes to converge
- Amount of disagreement between target function and learned boundary (final hypothesis)
    - Randomly generate test data
    - Label test data according to the target function and our hypothesis
    - Compare the assigned labels

