# Source: https://www.cantorsparadise.com/the-julia-set-e03c29bed3d0
import numpy as np

# Define the size & escape threshold
heightsize = 1080
widthsize = 1920
escapeno = 2

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

def julia_set1CN(c=0, height=heightsize, width=widthsize, x=0, y=0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5*height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom
    # Here the actual algorithm starts and the z paramter is defined for the Julia set function
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y
    # Initialize c to the complex number obtained from the quantum circuit
    c = np.full(z.shape, c)
    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)
    # To keep track on which points did not converge so far
    m = np.full(c.shape, True, dtype=bool)
    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m] 
        m[np.abs(z) > escapeno] = False 
        div_time[m] = i
    return div_time


def julia_set2CN1(c0=0, c1=0, height=heightsize, width=widthsize, x=0, y=0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5*height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom
    # Here the actual algorithm starts and the z paramter is defined for the Julia set function
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y
    # Initialize the c's to the complex amplitudes obtained from the quantum circuit
    c0 = np.full(z.shape, c0)
    c1 = np.full(z.shape, c1)
    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)
    # To keep track on which points did not converge so far
    m = np.full(c0.shape, True, dtype=bool)
    for i in range(max_iterations):
        z[m] = (z[m]**2 + c0[m]) / (z[m]**2 + c1[m]) # julia set mating 1
        m[np.abs(z) > escapeno] = False
        div_time[m] = i
    return div_time

def julia_set2CN2(c0=0, c1=0, height=heightsize, width=widthsize, x=0, y=0, zoom=1, max_iterations=100):
    # To make navigation easier we calculate these values
    x_width = 1.5
    y_height = 1.5*height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom
    # Here the actual algorithm starts and the z paramter is defined for the Julia set function
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y
    # Initialize the c's to the complex amplitudes obtained from the quantum circuit
    c0 = np.full(z.shape, c0)
    c1 = np.full(z.shape, c1)
    # To keep track in which iteration the point diverged
    div_time = np.zeros(z.shape, dtype=int)
    # To keep track on which points did not converge so far
    m = np.full(c0.shape, True, dtype=bool) 
    for i in range(max_iterations):
        z[m] = (c0[m]*z[m]**2 + 1 - c0[m]) / (c1[m]*z[m]**2 + 1 - c1[m]) # julia set mating 2
        m[np.abs(z) > escapeno] = False 
        div_time[m] = i
    return div_time
