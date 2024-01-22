# Mean Deficiency Correction Methods

This repository features Python implementations of different mean deficiency correction metrics. These metrics offer alternative solutions to address the limitations of the conventional arithmetic mean, especially when handling data with outliers or skewed distributions. 

The project aims to **provide organized Python code for indicators that can be utilized as effective alternatives or supplements to mitigate the drawbacks associated with traditional mean calculations.**

## Metrics 📌
This repository includes the following statistical metrics:

1. **Median Absolute Deviation(MAD)**: A measure of the spread of data points around the median. It is less sensitive to outliers compared to standard deviation.

- Function: `'median_absolute_deviation(data)'`

2. **Trimmed Mean**: Calculates the mean after excluding a certain proportion of data from both ends of the distribution.

- Function: `'trimmed_mean(data, proportiontocult=0.1, tail='both')'`

### Implementation Notes 📝: 
- The trimmed_mean() function is based on the trim_mean() function from the SciPy library.
- The `tail` parameter was added to allow trimming from either side of the distribution.
- The function only supports 1-dimensional arrays.


3. **Logarithmic Mean** : Takes the logarithm of the data before calculating the mean, which can help to mitigate the distortion caused by extreme values, especially in positively skewed distributions.

- Function: `'log_mean(data)'`

## Usage 💻
### Installation
1. Clone this repository:

```bash
git clone https://github.com/your-username/mean-deficiency-correction-methods.git
```

2. Install the required libraries:

```bash
pip install numpy pandas seaborn matplotlib
```

### Example Usage 
Refer to the 'example.py' file for a demonstration of how to use the implemented methods.
To run the example, simply execute the following command ⬇:

```bash
python example.py
```

## Additional Information 🔍
For more details on each method, refer to the corresponding function documentation within the mean_deficiency_correction.py file.
Consider the characteristics of your data and the specific goals of your analysis when selecting the most appropriate mean deficiency correction method.

## Contributions✨
This repository welcomes contributions and suggestions! Feel free to open issues or pull requests to improve the code or documentation 🤗


## References

* [Detect and deal with outliers](https://medium.com/@mert55yyyy/detect-and-deal-with-outliers-69b1e38ea1de)
* [Skewness, Kurtosis, and Normalization](https://medium.com/@p/27479be7a55b)
    * Skewness and kurtosis
* [MAD](https://medium.com/@n.j.marey/outlier-detection-median-absolute-deviation-in-sas-971e07f95b67)
* ['trim_mean' function of SciPy](https://github.com/scipy/scipy/blob/v1.12.0/scipy/stats/_stats_py.py#L3849-L3916)
* ['np.partition' function](https://numpy.org/doc/stable/reference/generated/numpy.partition.html)
* [Logarithm and log function](https://suppppppp.github.io/posts/Why-Series-MDM-1/)
