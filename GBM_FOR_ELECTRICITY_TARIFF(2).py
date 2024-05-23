
import numpy as np

def generate_GBM_from_data(array, n_paths, nsteps, total_time, xzero, seed=None):

    if seed is not None:
        np.random.seed(seed)
    
    log_returns = np.log(array[1:] / array[:-1])
    
    mu = np.mean(log_returns)

    n = len(log_returns)
    sigma = np.sqrt((np.sum((log_returns - mu) ** 2)) / (n - 1))
    
    
    def simulate_GBM(nsteps, total_time, mu, sigma, xzero):
        dt = total_time / nsteps
        steps = np.random.normal((mu - (sigma ** 2) / 2) * dt, sigma * np.sqrt(dt), nsteps)
        y = np.insert(np.cumprod(np.exp(steps)) * xzero, 0, xzero)  
        x = np.linspace(0, total_time, num=nsteps+1)  
        return x, y
    
    simulation_data = {'x': np.linspace(0, total_time, num=nsteps+1)}
    for i in range(n_paths):
        _, y = simulate_GBM(nsteps, total_time, mu, sigma, xzero)
        simulation_data[f'y{i}'] = y

    return simulation_data, mu, sigma
