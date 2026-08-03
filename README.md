# Gismeteo_parser
Gismeteo_parser - парсер сайта погоды Gismeteo предоставляет несколько вариантов вывода, а также динамически загружает погоду с доступных городов на сайте. Это мой первый масштабный проект, который был написан на python + requests + BeautifulSoup. Данный стек был выбран так как структура сайта была выстроена из html кода, который можно было парсить, используя библиотеку BeautifulSoup. 

После запуска программа предложит выбрать город из списка доступных на сайте:

<img width="864" height="579" alt="image" src="https://github.com/user-attachments/assets/0bb9f543-a49a-4e99-a792-98deb83ae8de" />

<img width="864" height="579" alt="image" src="https://github.com/user-attachments/assets/68f55e52-e761-4473-9324-de9ac90b5a5d" />

Затем будут предложены варианты вывода данных: 

<img width="656" height="314" alt="image" src="https://github.com/user-attachments/assets/716580c5-f8a6-4ffe-8e4a-7648402cf410" />

Существует 4 варианта вывода данных:

1 вариант: Погода на сегодня

<img width="943" height="199" alt="image" src="https://github.com/user-attachments/assets/efaf8d62-ce6a-49f7-9807-795bc1106a5c" />

2 вариант: Погода на завтра

<img width="943" height="188" alt="image" src="https://github.com/user-attachments/assets/6ce415ac-b263-4901-a381-2308097ec50a" />

3 вариант: Погода на 7 дней

<img width="943" height="476" alt="image" src="https://github.com/user-attachments/assets/a439394f-baf5-48b2-9e87-51f3c7ddcc04" />

4 вариант: Сохранить прогноз в CSV

<img width="807" height="398" alt="image" src="https://github.com/user-attachments/assets/03796a2b-0cf5-4525-b937-3d9a1db239e2" />

Последний вариант сохраняет данные в CSV файл, который вы можете открыть в любом удобном для вас редакторе.

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/whitecapman/Gismeteo_parser.git
   cd Gismeteo_parser
   ```
2. Установите зависимости:
  ```bash
  pip install -r requirements.txt
  ```
3. Запустите парсер:
  ```bash
  python parser.py
  ```
