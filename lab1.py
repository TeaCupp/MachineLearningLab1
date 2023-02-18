import statistics
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import pandas as pd



grades = [85, 93, 45, 89, 85]

print(f'Відсортований список: {sorted(grades)}')

print(f'Середнє значення, раховане ручним методом: {sum(grades)/len(grades)}')

print(f'Середнє значення, раховане за допомогою модуля statistics: {statistics.mean(grades)}')

print(f'Медіана, рахована за допомогою модуля statistics: {statistics.median(grades)}')

print(f'Мода, рахована за допомогою модуля statistics: {statistics.mode(grades)}')

print(f'Дисперсією генеральної сукупності: {statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])}')

print(f'Стандартне відхилення: {statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])}')

print(f'Стандартне відхилення, раховане ручним методом: {math.sqrt(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))}')

grades = pd.Series([87, 100, 94])
print(f'Виведення колекції Series з різними значеннями: \n{grades}')

print(f'Виведення колекції Series з однаковими значеннями: \n{pd.Series(98.6, range(3))}')

