import requests
import json

KEYWORDS = [
    "The Marvels",
    "Five Nights at Freddies",
    "Taylor Swift: Era's Tour",
    "Killers of the flower moon",
    "Priscilla",
    "The Holdovers",
    "After Death",
    "PAW Patrol: The Mighty Movie",
    "The Exorcist: Believer",
    "Journer to Bethlehem",
]
APIKEY = "e7e91eca2b244fc88a0b71323eea37d0"


def make_query():
    return " OR ".join([f'"{keyword}"' for keyword in KEYWORDS])


def main():
    print(make_query())
    data = requests.get(
        f"https://newsapi.org/v2/everything?q={make_query()}&apiKey={APIKEY}",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    if data.status_code == 200:
        json.dump(data.json(), open("all_keywords.json", "w"))


if __name__ == "__main__":
    main()
