from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

# data generation
X = np.random.rand(1000, 1)
y = 4 + 3 * X + .2 * np.random.randn(1000, 1) # noise added

# building Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((X, one), axis=1)

# linear regression solution by formula
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_lr = np.dot(np.linalg.pinv(A), b)
print("Solution found by formula w = ", w_lr.T)

# display result
w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 1, 2, endpoint=True)
y0 = w_0 + w_1 * x0

# draw the fitting line
plt.plot(X.T, y.T, 'b') # data
plt.plot(x0, y0, 'y', linewidth=2) # fitting line
plt.axis([0, 1, 0, 10])
plt.show()

# stochastic gradient descent for linear regression
def sgrad(w, i, rd_id, Xbar, y):
    true_i = rd_id[i]
    xi = Xbar[true_i, :]
    yi = y[true_i]
    a = np.dot(xi, w) - yi
    return(xi * a).shape(2, 1)

def sgd(w_init, eta, Xbar, y):
    w = [w_init]
    w_last_check = w_init
    iter_check_w = 10
    N = Xbar.shape[0]
    count = 0
    for it in range(10):
        # shuffle data
        rd_id = np.random.permutation(N)
        for i in range(N):
            count += 1
            g = sgrad(w[-1], i, rd_id, Xbar, y)
            w_new = w[-1] - eta * g
            w.append(w_new)
            if count % iter_check_w == 0:
                w_this_check = w_new
                if (np.linalg.norm(w_this_check - w_last_check) / len(w_init)) < 1e-3:
                    return w
                w_last_check = w_this_check
    return w

# initializing weights
w_init = np.array([[0], [0]])

# run stchastic gradient descent
eta = 0.01
w_sgd = sgd(w_init, eta, Xbar, y)
w_sgd_final = w_sgd[-1]
print("SGD Solution w = {}, obtained after {} iterations".format(w_sgd_final.rave(), len(w_sgd)))

"""
Plotting Results
"""
plt.figure(figsize=(14, 6))

# Plot for SGD result
plt.plot(X.T, y.T, 'b.')  # data
y_sgd = Xbar.dot(w_sgd_final)
plt.plot(X, y_sgd, 'r-', linewidth=2)  # the SGD fitting line
plt.plot(x0, y0, 'y', linewidth=2)  # the fitting line by formula
plt.axis([0, 1, 0, 10])
plt.show()