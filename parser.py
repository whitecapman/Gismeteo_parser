import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, ConnectionError, Timeout
from config import TIMEOUT, headers

def fetch_page(url):
    try:
        response=requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        print(response.url, response.status_code)
        
        data=response.text
    
    except HTTPError as http:
        print(f"Ошибка HTTP: {http}")
    
    except ConnectionError as ce:
       print(f"Ошибка соединения: {ce}")
    except Timeout as to:
        print(f"Превишено время ожидания: {to}")
    else:
        return data

def parse_page(data):
    soup=BeautifulSoup(data, 'lxml')
   
   # блок с датами
    row_date=soup.find("div", class_="widget-row widget-row-date")
    if not row_date:
        print("Не найден блок с датами")
        return None
    date_blocks=row_date.find_all("a") # все дни, где каждый это "a"

    # Блок с температурами
    chart=soup.find("div", class_="chart")
    if not chart:
        print("Не найден блок chart")
        return None
    values_div = chart.find("div", class_='values')
    
    if not values_div:
        print("Не найден блок values")
        return None
    value_blocks = values_div.find_all("div", class_="value")    
    
    # блок с состоянием погоды
    widget_row=soup.find("div", class_="widget-row widget-row-icon is-important")
    if not widget_row:
        print("Не найден блок widget_row")
        return None
    state_blocks=widget_row.find_all("div", class_="row-item")

    # Собираем в список словарей
    forecast = []
    for i in range(len(date_blocks)):
        date_block = date_blocks[i]
        value_block = value_blocks[i]
        state_block = state_blocks[i]

        # Извлекаем день недели и число
        day_tag = date_block.find("div", class_='day').text
        date_tag = date_block.find("div", class_="date")
        date_str = date_tag.text.strip() if date_tag else ""
        full_date = f"{day_tag} {date_str}"  # "Пн 31 июля"
        
         # Извлекаем температуры
        maxt_div = value_block.find("div", class_='maxt')
        mint_div = value_block.find("div", class_='mint')
        maxt = maxt_div.find("temperature-value").get("value") if maxt_div else None
        mint = mint_div.find("temperature-value").get("value") if mint_div else None
        
        # Извлекаем состояние погоды
        state_text=state_block.get("data-tooltip")

        forecast.append({
            "дата": full_date,
            "состояние": state_text,
            "температура-max": maxt,
            "температура-min": mint 
            })
        today=forecast[0]
    return {"forecast":forecast, 'today':today}

def get_urls(url):
    try:
        response=requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()

        print(response.url, response.status_code)
        
        data=response.text
    
    except HTTPError as http:
        print(f"Ошибка HTTP: {http}")
    
    except ConnectionError as ce:
        print(f"Ошибка соединения: {ce}")
   
    except Timeout as to:
        print(f"Превишено время ожидания: {to}")
    else:

        CITY_URLS={}

        soup=BeautifulSoup(data, 'lxml')
        list_cities = soup.find("div", class_="widget cities-popular").find("div", class_='list')
        cities = list_cities.find_all("a")

        for city in cities:
            city_name = city.text if city else None
            city_url = f"{url}{city.get('href')}weekly/"
            
            CITY_URLS[city_name]=city_url

        return CITY_URLS

        
