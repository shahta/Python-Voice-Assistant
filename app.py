from api_functions import *
import datetime
from time import sleep


def date_time():
    if 'time' in text:
        print(f'The current time is: {datetime.datetime.now().time()}')
    elif 'date' in text:
        print(f'The current date is: {datetime.datetime.now().date()}')


while True:
    print("For a list of operations I can perform simply say 'help'.")
    print("I'm listening... : ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(f'You said: {text}')
        if 'calories' in text:
            calorie_counter()
        elif 'help' in text:
            print("""
            'calories' - calculate calories in a food item
            'date' - returns the present date
            'time' - returns the current time
            'headlines' - returns the top headlines for the day
            'weather' - returns the current weather for a specified city
            'businesses' - returns the information for a specified business
            'open website' - launches a speciifed website
            'stocks' - asks for ticker symbol then returns the information for respective stock
            'quit' - shuts down voice assistant
            """)
        elif 'date' in text:
            date_time()
        elif 'time' in text:
            date_time()
        elif 'headlines' in text:
            print('')
            news()
        elif 'weather' in text:
            print('Which city would you like to retrieve weather information for? ')
            audio2 = r.listen(source)
            city = r.recognize_google(audio2)
            weather(city)
        elif 'businesses' in text:
            print('What type of business are you searching for? (Restaurants, barbers, pubs, etc.)')
            audio3 = r.listen(source)
            term = r.recognize_google(audio3)
            print(term)
            print('And which city are you looking for?')
            audio4 = r.listen(source)
            location = r.recognize_google(audio4)
            print(location)
            print('')
            business_search(term, location)
        elif 'open website' in text:
            print('What would you like to search? (youtube, espn, walmart, etc.)')
            audio5 = r.listen(source)
            query = r.recognize_google(audio5)
            print(f'Searching for {query}')
            open_app(query)
            sleep(10)
        elif 'stocks' in text:
            ticker = input('Specify the ticker symbol of the stock you are trying to retrieve information for: ')
            print(f'Showing results for {ticker}:')
            get_stock(ticker)
        elif 'quit' in text:
            print('Friday shutting down...')
            break
        else:
            print("I could not understand what you said.")




