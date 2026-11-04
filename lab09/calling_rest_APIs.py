import requests

url = "https://official-joke-api.appspot.com/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print(f"Joke: {joke['setup']}")
    print(f"Punchline: {joke['punchline']}")
else:
    print(f"Failed to retrieve joke. Status code: {response.status_code}")   