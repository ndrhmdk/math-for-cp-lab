from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt


def grad(X):
    return 4 * X * np.exp(2 * X**2 + 1) + 6 * X**2 - 18

def cost(X):
    return np.exp(2 * X**2 + 1) - 18 * X + 2 * X**3 - 5

def gradient_descent(alpha, x0, gra=1e-5, loop=10000):
    x = [x0]
    for it in range(loop):
        x_new = x[-1] - alpha * grad(x[-1])
        if abs(grad(x_new)) < gra:
            break
        x.append(x_new)
    return x, it

def visualize():
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(xlim=(-8, 8), ylim=(-10, 60))
    ax.text(-6, 55, '$f(x)=e^{2x^2+1} - 18x + 2x^3 - 5$')
    # label_1 = ax.text(-6, 50, '')
    # label_2 = ax.text(0, 30, '')

    line, = ax.plot([], [], 'ro-', lw=5)
    x = np.linspace(-8, 8, 100)
    y = cost(x)
    ax.plot(x, y)
    plt.show()

if __name__ == '__main__':
    (x, it) = gradient_descent(alpha=0.001, x0=5, gra=1e-5, loop=10000)
    print(f"x = {x[-1]}, f(x) = {cost(x[-1])}, iter = {it}")
    visualize()
