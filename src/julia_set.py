# Source: https://www.cantorsparadise.com/the-julia-set-e03c29bed3d0
import numpy as np

def julia_set(c = -0.835 - 0.2321 * 1j, num_iter = 50, 
              N = 1000, X0 = np.array([-2, 2, -2, 2])):
    """
    This function creates the Julia set. 
    Inputs 
        c: (complex) arbitrary complex number to add to the grid z.
        num_iter: (int) number of iterations to perform.
        N: (int) number of grid points on each axis of z.
        X0: (array) limits of the grid z.
    Outputs 
        x: (array) values of the real x-axis used in the grid.
        y: (array) values of the imaginary y-axis used in the grid.
        F: (array) the complex grid containing the Julia set.
    """     
    # Limits of the complex grid.
    x0 = X0[0] 
    x1 = X0[1]
    y0 = X0[2]
    y1 = X0[3]    # Set up the complex grid. Each element in the grid
    # is a complex number x + yi.
    x, y = np.meshgrid(np.linspace(x0, x1, N), 
                       np.linspace(y0, y1, N) * 1j)
    z = x + y    # F keeps track of which grid points are bounded
    # even after many iterations of z := z**2 + c.
    F = np.zeros([N, N])    # Iterate through the operation z := z**2 + c.
    for j in range(num_iter):
        z = z ** 2 + c
        index = np.abs(z) < np.inf
        F[index] = F[index] + 1    
    return np.linspace(x0, x1, N), np.linspace(y0, y1, N), F
