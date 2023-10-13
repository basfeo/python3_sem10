import pandas as pd
import random
# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Определение уникальных значений в столбце 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов на основе уникальных значений
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

data = data.drop('whoAmI', axis=1)  # Удаление исходного столбца

print(data.head())
