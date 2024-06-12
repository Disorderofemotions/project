import camelot
import pandas as pd
from sqlalchemy import create_engine

# Путь к PDF файлу
file_path = "b4.pdf"

# Чтение таблиц из PDF файла
tables = camelot.read_pdf(file_path, pages="all")

df_list = []
for table in tables:
    df = table.df
    if len(df.columns) > 5:
        df = df[[0, 1, 2, 3, 4, 5]]
        df.columns = ['№','Адрес', 'Период', 'Начислено', 'Оплачено', 'Суммаудержанноговознаграждения']
        
        df = df.dropna()
        df = df.drop(index=df.index[0], axis=0)
        df = df.drop(index=df.index[-1], axis=0)
        df = df.drop(columns=df.columns[0], axis=1)
        df = df.drop(columns=df.columns[1], axis=1)
        # Добавление обработанных столбцов
        df["Суммаудержанноговознаграждения"] = df["Суммаудержанноговознаграждения"].str.replace(' ', '')
        df["Начислено"] = df["Начислено"].str.replace(' ', '')
        df["Процент_вознаграждения"] = (df["Суммаудержанноговознаграждения"].str.replace(',', '.').astype(float) * 100 / df["Начислено"].str.replace(',', '.').astype(float)).round(decimals=1)

        # Добавление обработанной таблицы в список
        df_list.append(df)

final_df = pd.concat(df_list, ignore_index=True)

# Соединение с базой данных SQLite
engine = create_engine('sqlite:///output.db', echo=False)

# Сохранение данных в базу данных
final_df.to_sql('output123', con=engine, if_exists='replace', index=False)
