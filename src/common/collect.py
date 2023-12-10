import logging

import creds
from src.common.requestutils import send_resquest

logger = logging.getLogger(__name__)


def get_from_newsapi(query: str, session=None):
    """Get data from newsapi.org in english."""
    language = "en"

    url = "https://newsapi.org/v2/everything"

    params = {"q": query, "language": language, "apiKey": creds.API_KEY}

    data = send_resquest(url, params=params, session=session)

    if not data:
        raise ValueError("Request failed")
    elif data.status_code != 200:
        raise ValueError(data.reason)
    else:
        return data
