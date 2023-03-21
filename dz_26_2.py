import numpy as np
from scipy.stats import mode

# Вихідні дані - вибірка спостережень
data = [10, 13, 10, 9, 9, 12, 12, 6, 7, 9, 8, 9, 11, 9, 14, 13, 9, 8, 8, 7,
        10, 10, 11, 11, 11, 12, 8, 7, 9, 10, 14, 13, 8, 8, 9, 10, 11, 11, 12, 12]

# Побудова дискретного статистичного розподілу
unique_values, counts = np.unique(data, return_counts=True)
freqs = counts / len(data)
for value, freq in zip(unique_values, freqs):
    print(f"{value}: {freq:.3f}")

# Знаходження моди
mode_value, mode_count = mode(data)
print(f"Мода: {mode_value[0]}")

# Знаходження медіани
median = np.median(data)
print(f"Медіана: {median}")
