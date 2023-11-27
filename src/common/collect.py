import creds

from src.common.requestutils import send_resquest


def get_from_newsapi(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={creds.API_KEY}"

    data = send_resquest(url)

    if not data:
        raise ValueError("Request failed")
    elif data.status_code != 200:
        raise ValueError(data.reason)
    else:
        return data
