
from weather import Weather
weather = Weather()
def lookuplocation(city):
    location = weather.lookup_by_location(city)
    print(location)
    condition = location.condition() 

    
    #step 1: print the weather condition next 5 days
    forecasts = location.forecast()
    while len(forecasts) > 5:
        forecasts.pop()
    
    # step 2: print the day that has the higest tempeture and the day that has the lowest

    temp = []
    for item in forecasts:
        high_temp = item['high']
        temp.append(int(high_temp))



    for item in forecasts:
        if int(item['high']) == max(temp):
            print("The day that has higest tempeture next 5 days  in halifax is %s " % (item['date']))
            print("The higest tempeture next 5 days is %s " % (item['high']))
            print("The weather condition of the day that has higest tempeture next 5 days is %s " % (item['text']))

    for item in forecasts:
        if int(item['high']) == min(temp):
            print("The day that has lowest tempeture next 5 days in halifax is %s " % (item['date']))
            print("The lowest tempeture next 5 days is %s " % (item['high']))
            print("The weather condition of the day that has lowest tempeture next 5 days is %s " % (item['text']))
#step 3: if it will rain the next 5 days inform the user and tell him which day it will rain
        elif item['text'] == 'rain':
            print("The day that will be rainy is " % (item['date']))




lookuplocation('halifax')

