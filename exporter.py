import csv
from datetime import datetime

def save_to_csv(forecast_data, city_name, filename=None): # информация, город - ну это для названия.
    if filename is None:
        cdatetime=datetime.now().strftime("%Y-%m-%d")
        filename=f"weather_{city_name}_{cdatetime}.csv" # даём название файлу
    with open(filename, "w", newline='', encoding='utf_8') as f: # запись 
        writer = csv.DictWriter(f, fieldnames=["дата", "состояние", "температура-max", "температура-min"]) # даём заголовки (те же что и в словаре)
        writer.writeheader()
        writer.writerows(forecast_data)
    return filename
