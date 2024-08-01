import requests

location = input('Enter the city or location : ')
api = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=06c921750b9a82d8f5d1294e1586276f"

json_data = requests.get(api).json()

if json_data['cod']=='404':
    print('no city found')
else:    
    temp = int(json_data['main']['temp'] - 273.15)
    temp_f=(temp*9/5)+32
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    weather=json_data['weather'][0]['main']
    temp_type=input("enter c/C to see temperature in celsius and f/F for farenheit ")
    if temp_type=='c' or temp_type=='C':
        print(f"Temperature in {location} is {temp} degree Celsius")
    elif temp_type=='f' or temp_type=='F':  
        print(f"Temperature in {location} is {temp_f} degree Farenheit")
    print('Presure is:', pressure)
    print('Humidity is:',humidity)
    print('Wind speed is:',wind)
    print('Weather is:',weather)