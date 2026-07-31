import requests
from config import API_KEY


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            return {"error": "City not found."}

        elif response.status_code == 401:
            return {"error": "Invalid API Key."}

        else:
            return {"error": f"Error {response.status_code}"}

    except requests.exceptions.ConnectionError:
        return {"error": "No Internet Connection."}

    except requests.exceptions.Timeout:
        return {"error": "Request Timed Out."}

    except Exception as e:
        return {"error": str(e)}