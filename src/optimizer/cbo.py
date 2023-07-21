import numpy as np
from tqdm.notebook import tqdm


def compute_valpha(V, alpha, function):
    # computation of current empirical consensus point v_alpha
    E = np.array([function(el) for el in V]) 
    Emin = np.min(E)

    w_alpha = np.exp(-alpha * (E - Emin))
    v_alpha = np.sum(V * w_alpha / np.sum(w_alpha), axis=0) 

    return v_alpha



def CBO_optimizer(function, boundaries, delta_t, sigma, alpha, d, N, nt, lambda_=1):
    '''
    function: function to be optimized
    boundaries: boundaries of the function
    delta_t: time step
    sigma: standard deviation of the noise
    alpha: learning rate
    d: dimension of the function
    N: number of particles
    nt: number of iterations
    '''
    
    # initialize particles
    V = np.random.uniform(boundaries[0], boundaries[1], (N, d))
    history = [V]

    for t in tqdm(range(nt)):
        # generate noise from Brownian motion
        B = np.random.normal(0, delta_t, (N, d)) # covariance matrix should be delta_t * I

        # calculate current consensus value
        v_alpha = compute_valpha(V, alpha, function)

        # consensus drift term
        V = V - delta_t * lambda_ * (V - v_alpha) + sigma * np.abs(V - v_alpha) * B
        
        history.append(V)
    return v_alpha, history 
