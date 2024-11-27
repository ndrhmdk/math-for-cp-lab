import numpy as np
import matplotlib.pyplot as plt

def grad(X):
    return 2*X + 10*np.cos(X)

def cost(X):
    return X**2 + 10*np.sin(X)

# check convergence
def has_converged(theta_new, grad):
    return (np.linalg.norm(grad(theta_new)) / len(theta_new)) < 0.001

# gradient descent with momentum
def gdm(theta_init, alpha=0.1, beta=0.9):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)

    for it in range(1000):
        v_new = beta * v_old + alpha * grad(theta[-1])
        theta_new = theta[-1] - v_new
        theta.append(theta_new)
        v_old = v_new

    return (theta, it)

def gd(x0, alpha=0.1, gra=1e-3, loop=1000):
    x = [x0]
    for it in range(loop):
        x_new = x[-1] - alpha * grad(x[-1])
        if abs(grad(x_new)) < gra:
            break
        x.append(x_new)
    return (x, it)

if __name__ == '__main__':
    (x1, it1) = gd(5, 0.1)
    print(f"Gradient Descent Solution - x1 = {x1[-1]}, cost = {cost(x1[-1])}, obtained after {it1} iteration(s)")

    (x2, it2) = gdm(5, 0.1, beta=0.9)
    print(f"Gradient Descent with Momentum Solution - x2 = {x2[-1]}, cost = {cost(x2[-1])}, obtained after {it2} iteration(s)")

    x_vals = np.linspace(-7, 7, 1000)
    y_vals = cost(x_vals)

    plt.figure(figsize=(14, 6))

    # visualization for Gradient Descent
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label='Cost Function')
    plt.plot(x1, [cost(x) for x in x1], 'ro-', label='Gradient Descent Trajectory')
    plt.title('Gradient Descent')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # visualization for Gradient Descent with Momentum
    plt.subplot(1, 2, 2)
    plt.plot(x_vals, y_vals, label='Cost Function')
    plt.plot(x2, [cost(x) for x in x2], 'ro-', label='Momentum Trajectory')
    plt.title('Gradient Descent with Momentum')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    plt.show()
