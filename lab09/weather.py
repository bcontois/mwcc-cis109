import requests
import argparse



def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit" : 1
    }

    headers = {
        "User-Agent": "MWCC 1.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        coordinates = response.json()
        lat = coordinates[0]['lat']
        lon = coordinates[0]['lon']
        return lat, lon

def get_noaa_endpoint(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_url = data['properties']['forecast']
        print(f"NOAA Forecast URL: {forecast_url}")
        return forecast_url
    else:
        print(f"Failed to retrieve NOAA endpoint. Status code: {response.status_code}")
        return None 

def get_noaa_forecast(url):
    response = requests.get(url)

    if response.status_code == 200:
        forecast_data = response.json()
        periods = forecast_data['properties']['periods']
        print("Weather Forecast:")
        for period in periods:
            print(f"{period['name']}: {period['detailedForecast']}")
    else:
        print(f"Failed to retrieve NOAA forecast. Status code: {response.status_code}")  

def main():

    parser = argparse.ArgumentParser()

    # Requires a message to encrypt or decrypt depending on the value of the shift entered.
    parser.add_argument ("-l", "--encrypt", action='store_true', required=False, help="Encrypt The Message.")
    parser.add_argument ("-d", "--decrypt", action='store_true', required=False, help="Decrypt The Message.")
    parser.add_argument ("-w", "--message", required=True, help="The message to encrypt/decrypt.")
    parser.add_argument ("-a", "--shift", required=True, help="The Shift Offest Value for the Caesar Cypher.")
    args = parser.parse_args()

    coordinates = get_coordinates("Millbury, MA")

    print(f"Coordinates: {coordinates}")
    lat = coordinates[0]
    lon = coordinates[1]

    url = get_noaa_endpoint(lat, lon)
    print(url)

    forecast = get_noaa_forecast(url)
    print(forecast)

    #pass in city name


if __name__ == "__main__":
    main()

# 1. The program, weather.py, MUST accept a "City, State" string as a command-line option -l (--location)
#   command-line option -d (--detailed) that returns the current day or night's temperature and detailed forecast.
# 6. The program MUST include a command-line option -w (--week) that returns the short weather forecast for the next week.
# 7.  The program MUST include a command-line option -a (--average) that compiles each period's temperature into a list and uses Python's built-in sum and len functions to calculate and return the expected average temperature of all the days contained within the weather forecast.
# 8. All program output MUST be professionally formatted.

#iterate through forecast that 