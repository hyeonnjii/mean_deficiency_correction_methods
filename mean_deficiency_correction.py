import numpy as np

def median_absolute_deviation(data):
    """
    Calculate Median Absolute Deviation (MAD).

    Parameters
    ----------
    data : array_like
        Input data(e.g., list, array, or other array-like objects).

    Returns
    -------
    mad_value : float
        Median Absolute Deviation.

    Notes
    -----
    MAD is less sensitive to outliers and measures the spread of the data.
    Useful when mean and standard deviation are strongly influenced by outliers.

    Example
    -------
    >>> data = [1, 2, 3, 4, 5, 1000]
    >>> mad_value = median_absolute_deviation(data)
    >>> print(f"MAD: {mad_value}")
    MAD: 1.5
    """
    if data.size == 0:
        return np.nan

    median_value = np.median(data)
    mad_value = np.median(np.abs(data - median_value))
    return mad_value

def trimmed_mean(data, proportiontocut=0.1, tail='both'):
    """
    Calculate Trimmed Mean.

    Parameters
    ----------
    data : array_like
        Input data.
    proportiontocut : float, optional
        Proportion of data to exclude from both ends (default is 0.1).
    tail : {'both', 'left', 'right'}, optional
        Determines which end(s) of the data to exclude (default is 'both').

    Returns
    -------
    trimmed_mean_value : float
        Trimmed Mean.

    Raises
    ------
    ValueError
        If the input data is empty.
    
    Notes
    -----
    Calculate the mean by excluding a certain proportion of data from both ends.
    Use the 'tail' parameter to exclude data from the left or right side.

    Example
    -------
    >>> data = [1, 2, 3, 4, 5, 1000]
    >>> trimmed_mean_value = trimmed_mean(data, proportiontocut=0.2, tail='right')
    >>> print(f"Trimmed Mean: {trimmed_mean_value}")
    Trimmed Mean: 3.0
    """
    data = np.asarray(data)
    
    if data.size == 0:
        raise ValueError("Input data must not be empty.")
    
    nobs = len(data)

    lowercut = int(proportiontocut * nobs)
    uppercut = nobs - lowercut
    
    atmp = np.partition(data, (lowercut, uppercut - 1))

    if tail == 'left':
        return np.mean(atmp[lowercut + 1:])
    elif tail == 'right':
        return np.mean(atmp[:uppercut])
    else: 
        return np.mean(atmp[lowercut+1:uppercut])
    

def log_mean(data):
    """
    Calculate Logarithmic Mean and transform it back to the original scale.

    Parameters
    ----------
    data : array_like
        Input data (e.g., list, array, or other array-like objects).

    Returns
    -------
    Tuple: float, float
        Logarithmic Mean and Original Scale Mean (exponential transformation of log_mean_value)

    Notes
    -----
    Useful for asymmetric or skewed distributions, especially when dealing with large values.
    Mainly applicable to datasets with positive values.
    Transforms positive distributions to log distributions, making them closer to normal distributions.
    Mitigates the impact of relative size differences in data, reducing variance.
    Used for correction in nonlinear relationships, e.g., transforming exponential growth to a linear relationship.
    Commonly applied in finance (e.g., returns, stock prices), biological data (e.g., cell growth rates, gene expression),
    and marketing/sales data (e.g., revenue, customer counts).

    Example
    -------
    >>> data = [1, 2, 3, 4, 5, 1000]
    >>> log_mean_result = log_mean(data)
    >>> print(f"Log Mean: {log_mean_result[0]}")
    >>> print(f"Original Scale Mean: {log_mean_result[1]}")
    Log Mean: 2.2480009985542204
    Original Scale Mean: 9.46878878260777
    """
    log_data = np.log1p(data)
    log_mean_value = np.mean(log_data)
    original_scale_value = np.exp(log_mean_value)
    return log_mean_value, original_scale_value


