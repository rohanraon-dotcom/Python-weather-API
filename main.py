from weather import get_weather


print("-" * 38)
print("         WEATHER APPLICATION")
print("-" * 38)

city = input("Enter City Name: ")

weather = get_weather(city)

if "error" in weather:
    print("\nError:", weather["error"])

else:
    city_name = weather["name"]
    country = weather["sys"]["country"]

    temperature = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]

    humidity = weather["main"]["humidity"]
    pressure = weather["main"]["pressure"]

    wind_speed = weather["wind"]["speed"]

    condition = weather["weather"][0]["description"]

    print("\n========== WEATHER REPORT ==========")

    print(f"City         : {city_name}")
    print(f"Country      : {country}")

    print(f"Temperature  : {temperature} °C")
    print(f"Feels Like   : {feels_like} °C")

    print(f"Humidity     : {humidity}%")
    print(f"Pressure     : {pressure} hPa")

    print(f"Wind Speed   : {wind_speed} m/s")

    print(f"Condition    : {condition.title()}")

    print("====================================")