import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mean_deficiency_correction import median_absolute_deviation, trimmed_mean, log_mean

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
log_mean_result = log_mean(tips_data)

# Results ------------
print(f"Original Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"MAD: {mad_value}")
print(f"Trimmed Mean: {trimmed_mean_value}")
print(f"Log Mean: {log_mean_result[0]}")
print(f"Original Scale Mean: {log_mean_result[1]}")


