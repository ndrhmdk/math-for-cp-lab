import numpy as np
import matplotlib.pyplot as plt

def grad(X):
    return 4 * X * np.exp(2 * X**2 + 1) + 6 * X**2 - 18

def cost(X):
    return np.exp(2 * X**2 + 1) - 18 * X + 2 * X**3 - 5

def has_converged(grad_value, threshold=1e-3):
    return np.linalg.norm(grad_value) < threshold

def gdm(theta_init, alpha=0.1, beta=0.9, gra=1e-3, loop=1000):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)

    for it in range(loop):
        g = grad(theta[-1])
        v_new = beta * v_old + alpha * g
        theta_new = theta[-1] - v_new
        theta.append(theta_new)
        if has_converged(g, gra):
            break
        v_old = v_new

    return (theta, it)

def gd(x0, alpha=0.1, gra=1e-3, loop=1000):
    x = [x0]
    for it in range(loop):
        g = grad(x[-1])
        x_new = x[-1] - alpha * g
        if abs(g) < gra:
            break
        x.append(x_new)
    return (x, it)

if __name__ == '__main__':
    (x1, it1) = gd(np.array(5), 0.1)
    print(f"Gradient Descent Solution - x1 = {x1[-1]}, cost = {cost(x1[-1])}, obtained after {it1} iteration(s)")

    (x2, it2) = gdm(np.array(5), 0.1, beta=0.9)
    print(f"Gradient Descent with Momentum Solution - x2 = {x2[-1]}, cost = {cost(x2[-1])}, obtained after {it2} iteration(s)")

    x_vals = np.linspace(-7, 7, 1000)
    y_vals = cost(x_vals)

    plt.figure(figsize=(14, 6))

    # Visualization for Gradient Descent
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label='Cost Function')
    plt.plot(x1, [cost(x) for x in x1], 'ro-', label='Gradient Descent Trajectory')
    plt.title('Gradient Descent')
    plt.xlabel('x')
    plt.ylabel('Cost')
    plt.legend()

    # Visualization for Gradient Descent with Momentum
    plt.subplot(1, 2, 2)
    plt.plot(x_vals, y_vals, label='Cost Function')
    plt.plot(x2, [cost(x) for x in x2], 'ro-', label='Momentum Trajectory')
    plt.title('Gradient Descent with Momentum')
    plt.xlabel('x')
    plt.ylabel('Cost')
    plt.legend()

    plt.show()