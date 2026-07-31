import csv
from datetime import datetime

def save_to_csv(forecast_data, city_name, filename=None):
    if filename is None:
        cdatetime=datetime.now().strftime("%Y-%m-%d")
        filename=f"weather_{city_name}_{cdatetime}.csv"
    with open(filename, "w", newline='', encoding='utf_8') as f:
        writer = csv.DictWriter(f, fieldnames=["дата", "состояние", "температура-max", "температура-min"])
        writer.writeheader()
        writer.writerows(forecast_data)
    return filename
