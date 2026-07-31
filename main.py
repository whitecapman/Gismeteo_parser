import time
from parser import fetch_page, parse_page, get_urls
from InquirerPy import inquirer  # Импортируем сам интерактивный интерфейс
from exporter import save_to_csv
from config import base_url

def select_city():
    # Напрямую создаем и отображаем список выбора
    chosen_city = inquirer.select(
        message="Выберите город:",
        choices=list(CITY_URLS.keys()),
    ).execute()
    
    return chosen_city # выбранный город

if __name__ == "__main__":
    CITY_URLS=get_urls(base_url) # получаем url
    chosen_city = select_city() # сохраняем ответ в переменной
    url = CITY_URLS[chosen_city] # берем url по ключу
    print(f"выбран {chosen_city}: {url}")
    html=fetch_page(url) # ну это html код страницы
    
    if html:
        some_data=parse_page(html)
        # save_to_csv(some_data, chosen_city)
        action = inquirer.select(
            message="Выберите интервал: ",
            choices=[
                "Погода на сегодня",
                "Погода на завтра",
                "Погода на 7 дней",
                "Скачать прогноз на 7 дней"
                ]).execute()
        
        if action == "Погода на сегодня":
            print(f"Текущая погода в городе {chosen_city}: ")
            today=some_data["today"]
            print(f"Дата: {today['дата']}; состояние: {today['состояние']}; температура(max): {today['температура-max']}; температура(min): {today['температура-min']}")
        
        elif action == "Погода на завтра":
            tommorow_weather=some_data["forecast"]
            tommorow_weather=tommorow_weather[1]
            print(f"Погода на завтра в городе {chosen_city}")
            print(f"Дата: {tommorow_weather['дата']}; состояние: {tommorow_weather['состояние']}; температура(max): {tommorow_weather['температура-max']}; температура(min): {tommorow_weather['температура-min']}")
       
        elif action == "Погода на 7 дней":
            week_weather=some_data['forecast']
            for day in week_weather:
                print(f"Погода на {day['дата']}: ")
                print(f"Состояние: {day['состояние']}; температура(max): {day['температура-max']}, температура(min): {day['температура-min']}")
        
        elif action == "Скачать прогноз на 7 дней":
            save_to_csv(some_data['forecast'], chosen_city)

    else:
        print("Неизвестная ошибка: не удалось получить html код")


