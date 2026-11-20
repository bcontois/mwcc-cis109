import requests

# main() : Main entry point.

def main():
    pass

def get_coordinates(city):
    pass   

def get_noaa_endpoint(lat, lon):
    url = "https://api.weather.gov/points/42.5763523,-71.9952737"

    response = requests.get(url)

    if response.status_code == 200:
        forecastURL = response.json()
        print(f"ForecastURL: {forecastURL['forecast']}")
    else:
        print(f"Failed to retrieve ForecastURL. Status code: {response.status_code}")   

def get_noaa_forecast(url):
    pass  


# hardcoded lat / long for the get_noaa URLs

# parameter list for request function

# get_coordinates(city) : Retrieves lat/lon coordinates from REST API.
# get_noaa_endpoint(lat, lon) : Retrieves NOAA endpoint from REST API.
# get_noaa_forecast(url) : Retrieves the NOAA weather forecast.