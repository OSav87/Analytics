import pandas as pd
from pathlib import Path

path = Path('path_to_folder')

df = pd.DataFrame() # создаем пустой df, куда будут писаться наши данные

for csv_path in path.glob('**/*.csv'):
    temp_df = pd.read_csv(csv_path)

    # извлекаем дату и имя если нужно
    date = path.parts[-3]
    name = path.parts[-2]

    # Добавляем колонки
    temp_df['date'] = date
    temp_df['name'] = name

    # объединям наши датафреймы
    df = pd.concat([df, temp_df])