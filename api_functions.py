import speech_recognition as sr
import requests
from selenium import webdriver


def calorie_counter():
    number_of_items = int(input("How many items would you like to enter: "))
    count = 0
    total_calories = 0

    r = sr.Recognizer()
    while count < number_of_items:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(f'You said {text}')
                app_key = 'df529a77e5535ffd7c8016e975f3ab06'
                app_id = '62c6a906'
                response = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?ingr={text}&app_id={app_id}&app_key={app_key}')
                calories = response.json()['parsed'][0]['food']['nutrients']['ENERC_KCAL']
                print(f'This has {calories} calories.')
                total_calories += calories
                print(f'Your total calorie count is: {total_calories} calories')
                count += 1
        except LookupError:
            print('I could not understand what you said or this item is not in the database.')


def news():
    api_key = "4ebb5277f84c45079b4f421693cc9949"
    response = requests.get(f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={api_key}')
    cleaned = response.json()['articles']
    for item in cleaned:
        print(item['source']['name'])
        print(item['author'])
        print(item['title'])
        print(item['description'])
        print(item['url'])
        print('')


def weather(city):
    api_key = '1bcdcd394786d78fa6a3c97117016c09'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}')
    cleaned = response.json()
    print(f'Showing conditions for {city}')
    print('Conditions:')
    print(cleaned['weather'][0]['description'])
    print('Temperature (feels like): ')
    temp = cleaned['main']['temp']
    print(f'{temp}°C')


def business_search(term, location):
    api_key = '-5vfZY_p7Q_adE7UGB7LEd0oWTVc7swnO-psL6_jh05PysYnjfwd_LB0cPxmo9VBuqPn6f_YbT6jjEmiH_dHpiUhQM9EpOJ1cjPogPyDOnH-5UCuKbc-wG1DtYPEXnYx'
    headers = {'Authorization': 'Bearer ' + api_key}
    params = {'location': location, 'term': term}
    response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)
    cleaned = response.json()
    businesses = cleaned['businesses']
    for item in businesses:
        print(item['name'])
        print(item['location']['address1'])
        print(item['phone'])
        print('')


def open_app(query):
    browser = webdriver.Chrome()
    browser.get('https://www.google.com/')
    search = browser.find_element_by_name('q')
    search.send_keys(query)
    search.submit()


def get_stock(ticker_symbol):
    api_key = "ZOTA5511YU4N0XKB"
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker_symbol}&interval=60min&apikey={api_key}")
    json = response.json()['Time Series (60min)']
    for item in json:
        date = item
        opn = json[item]["1. open"]
        high = json[item]["2. high"]
        low = json[item]["3. low"]
        close = json[item]["4. close"]
        volume = json[item]["5. volume"]
        print(f"""Company: {ticker_symbol}
Date: {date}
Open: ${opn}
High: ${high}
Low: ${low}
Close: ${close}
Volume: {volume}""")
        break


