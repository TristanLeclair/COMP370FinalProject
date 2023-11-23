import requests


def send_resquest(url):
    data = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    if data.status_code == 200:
        return data
    else:
        return None


def make_query_or(KEYWORDS):
    return " OR ".join([f'"{keyword}"' for keyword in KEYWORDS])


def make_query_and(KEYWORDS):
    return " AND ".join([f'"{keyword}"' for keyword in KEYWORDS])
