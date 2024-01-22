# Mean Deficiency Correction Methods

This repository contains Python implementations of various mean deficiency correction methods, which are designed to address the limitations of the traditional arithmetic mean when dealing with data that contains outliers or skewed distributions.

## Methods
This repository includes the following mean deficiency correction methods:

1. **Median Absolute Deviation(MAD)**: A measure of the spread of data points around the median. It is less sensitive to outliers compared to standard deviation.

#### Function: `'median_absolute_deviation(data)'`

2. **Trimmed Mean**: Calculates the mean after excluding a certain proportion of data from both ends of the distribution.

#### Function: `'trimmed_mean(data, proportiontocult=0.1)'`

3. **Logarithmic Mean** : Takes the logarithm of the data before calculating the mean, which can help to mitigate the distortion caused by extreme values, especially in positively skewed distributions.

#### Function: `'log_mean(data)'`

## Usage

### Installation
1. Clone this repository:

```bash
git clone https://github.com/your-username/mean-deficiency-correction-methods.git
```

2. Install the required libraries:

```bash
pip install numpy pandas seaborn matplotlib scipy
```

3. Example Usage
Refer to the example.py file for a demonstration of how to use the implemented methods:

