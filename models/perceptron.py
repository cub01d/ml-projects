# load libraries
import numpy as np


# define our perceptron class
class Perceptron:
    def __init__(self):
        # choose random line
        a = np.random.uniform(-1, 1, 2)
        b = np.random.uniform(-1, 1, 2)

        # normal vector for target function weights
        dy = b[1] - a[1]
        dx = b[0] - a[0]
        self.f = np.array([[-dy, dx]]).reshape(2, 1)

        # fT dot a = t, where a is a point on line
        t = np.dot(self.f.T, a)[0]
        self.f = np.insert(self.f, 2, t, axis=0)
        
        # now we have the target function!
    
    def train(self, N):
        # generate training data
        X = np.random.uniform(-1, 1, (2, N))
        # insert x0=1 at the end to simplify threshold
        XX = np.insert(X, 2, 1, axis=0)
        assert(XX.shape == (3, N))

        # label training data
        y = np.sign(np.dot(self.f.T, XX))[0]
        
        # perceptron learning algorithm
        self.w = np.zeros([3,1])
        yhat = np.sign(np.dot(self.w.T, XX))

        # misclassified point indexes
        m = np.where(y != yhat)[1]
        
        i = 0
        while True:
            i += 1

            # break if converged
            if len(m) == 0:
                break

            # not converged: pick random misclassified point
            r = np.random.randint(0, len(m))
            index = m[r]
            point = XX.T[index].reshape(3,1)

            # update weight vector
            self.w = self.w + y[index]*point

            # update yhat
            yhat = np.sign(np.dot(self.w.T, XX))

            # update misclassified points
            m = np.where(y != yhat)[1]
        
        return i
        
    def test(self, n=5000):
        # generate n test data points in test data set
        points = np.random.uniform(-1, 1, (2, n))
        points = np.insert(points, 2, 1, axis=0)
        labels = np.sign(np.dot(self.f.T, points))
        
        yhat = np.sign(np.dot(self.w.T, points))
        error = np.where(yhat != labels)[0].size
        
        return error/n
    
    numtrials = 1000
N = 10
iterations = 0
errors = 0

for i in range(numtrials):
    # create a new perceptron
    p = Perceptron()
    iterations += p.train(N)
    errors += p.test()
    
print("avg # of iterations:", iterations/numtrials)
print("avg probability:", errors/numtrials)
