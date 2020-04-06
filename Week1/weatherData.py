import requests

# Use the TOKEN provided to you for the openweather API
API_TOKEN = 'TOKEN'

def getCityWeather(city_name):
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_TOKEN
    response = requests.get(url)
    json_data = response.json()
    city_temp = json_data['main']['temp']
    city_humidity = json_data['main']['humidity']
    print(city_name + ' has a temperature of ' + str(city_temp) + ' and a humidity of ' + str(city_humidity) + '%')

def main():
    city_list = [inp for inp in input('Enter City List : \n').split()]
    for city in city_list:
        getCityWeather(city)

if __name__ == '__main__':
    main()

# Refer to https://openweathermap.org/current for documentation of the API used 
