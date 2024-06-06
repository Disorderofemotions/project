import camelot
import pandas as pd

# Путь к PDF файлу
file_path = "b4.pdf"

# Чтение таблиц из PDF файла
tables = camelot.read_pdf(file_path, pages="all")

df_list = []
for table in tables:
 df = table.df
if len(df.columns) > 5:
 df = df[[0, 1, 2, 3, 4, 5]]
 # Переименование столбцов
df.columns = ['№','Адрес', 'Период', 'Начислено', 'Оплачено', 'Агентское вознаграждение']

# Удаление строк с пустыми значениями
df = df.dropna()
#  # Извлечение числовых значений из столбцов "Начислено" и "Агентское вознаграждение"
# df['Начислено'] = df['Начислено'].str.extract('(\d+.\d+)')
# df['Агентское вознаграждение'] = df['Агентское вознаграждение'].str.extract('(\d+.\d+)')

# # Преобразование значений в числовой формат
# df['Начислено'] = pd.to_numeric(df['Начислено'])
# df['Агентское вознаграждение'] = pd.to_numeric(df['Агентское вознаграждение'])

# Расчет процентного вознаграждения
# df['Процент вознаграждения'] = (df['Агентское вознаграждение'] / df['Начислено']) * 100

 # Добавление обработанной таблицы в список
df_list.append(df)
final_df = pd.concat(df_list, ignore_index=True)

final_df.to_excel("output72132.xlsx", index=False)