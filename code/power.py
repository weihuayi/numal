import numpy as np
from numpy.linalg import inv, norm, solve

def power_eig(
        A,
        x0=None,
        tol=1e-6,
        maxit=1000):
    M, N = A.shape
    if M != N:
        raise ValueError("The numbers of row and col of A are not equal!")
    if x0 is None:
        x0 = np.random.rand(N)
        x0 /= norm(x0)

    for k in range(maxit):
        y = A@x0
        x1 = y/norm(y)
        mu = x1@A@x1
        print(k, ": ", mu)

        diff = norm(x1 - x0)/norm(x0)
        if diff < tol:
            break
        else:
            x0 = x1

    return mu, x0

def inv_power_eig(
        A,
        x0=None,
        sigma=None,
        tol=1e-6,
        maxit=1000):
    M, N = A.shape
    if M != N:
        raise ValueError("The numbers of row and col of A are not equal!")
    if x0 is None:
        x0 = np.random.rand(N)
        x0 /= norm(x0)

    if sigma is not None:
        A -= sigma*np.eye(N)

    for k in range(maxit):
        y = solve(A, x0)
        x1 = y/norm(y)
        mu = x1@A@x1
        print(k, ": ", mu)
        diff = norm(x1 - x0)/norm(x0)
        if diff < tol:
            break
        else:
            x0 = x1

    if sigma is not None:
        mu = 1/mu + sigma
    else:
        mu = 1/mu
    return mu, x0

def rayleigh_eig(
        A,
        x0=None,
        tol=1e-6,
        maxit=1000):
    M, N = A.shape
    if M != N:
        raise ValueError("The numbers of row and col of A are not equal!")
    if x0 is None:
        x0 = np.random.rand(N)
        x0 /= norm(x0)
    sigma = x0@A@x0
    for k in range(maxit):
        y = solve(A - sigma*np.eye(N), x0)
        x1 = y/norm(y)
        mu = x1@A@x1
        if np.abs(mu - sigma) < tol:
            break
        else:
            sigma = mu
            x0 = x1
        print(k, ": ", sigma)
    return sigma, x0

def qr_iteration(A, maxit=1000):
    for k in range(maxit):
         Q, R = np.linalg.qr(A)
         A = R@Q
         print(k, ":\n")
         print(A)

# np.random.seed(10)
D = np.diag([10, 10, 3])
N = D.shape[0]
V = np.random.rand(N, N)
A = V@D@inv(V)

qr_iteration(A, maxit=100)

