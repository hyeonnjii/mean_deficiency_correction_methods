import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    Calculate Logarithmic Mean.

    Parameters
    ----------
    data : array_like
        Input data (e.g., list, array, or other array-like objects).

    Returns
    -------
    log_mean_value : float
        Logarithmic Mean.

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
    >>> log_mean_value = log_mean(data)
    >>> print(f"Log Mean: {log_mean_value}")
    Log Mean: 2.2480009985542204
    """
    log_data = np.log1p(data)
    log_mean_value = np.mean(log_data)
    return log_mean_value




# Load the 'tips' dataset in Seaborn
tips_data = sns.load_dataset('tips')

# Visualization
sns.histplot(tips_data['total_bill'], bins='auto', kde=True)
plt.title('Distribution of Total Bill Amounts')
plt.xlabel('Total Bill Amount')
plt.ylabel('Frequency')
plt.show()


tips_data = tips_data['total_bill']
# Calculate each metric
mean_value = np.mean(tips_data)
median_value = np.median(tips_data)
mad_value = median_absolute_deviation(tips_data)
trimmed_mean_value = trimmed_mean(tips_data, tail='right')
log_mean_value = log_mean(tips_data)

# Results ------------
print(f"Original Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"MAD: {mad_value}")
print(f"Trimmed Mean: {trimmed_mean_value}")
print(f"Log Mean: {log_mean_value}")

