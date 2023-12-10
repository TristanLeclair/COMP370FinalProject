import logging

import creds
from requests_cache.session import CachedSession
from src.common.requestutils import make_query_and, make_query_or, send_resquest

logger = logging.getLogger(__name__)


def get_from_api(keywords: list, is_or_query=True, use_cache=True, pages=1):
    """Get data from newsapi.org in english."""
    language = "en"

    query = make_query_or(keywords) if is_or_query else make_query_and(keywords)

    url = "https://newsapi.org/v2/everything"

    params: dict = {
        "q": query,
        "language": language,
        "apiKey": creds.API_KEY,
    }

    all_articles = []
    cache = retrieve_cache(name="newsapi") if use_cache else None

    for page in range(pages):
        params["page"] = page + 1
        data = send_resquest(url, params, cache=cache)
        if not data:
            logger.warning("No data")
            break
        elif data.status_code != 200:
            if data.status_code == 426 or data.status_code == 429:
                logger.warning("Rate limit reached")
                break
            raise ValueError(data.reason)
        all_articles.append(data.json())

    return all_articles


def retrieve_cache(name: str) -> CachedSession:
    """Use a cached session.
    Returns:
        CachedSession: A cached session.
    """

    return CachedSession(
        name + "_cache",
        ignored_parameters=["apiKey"],
        expire_after=3600,
        backend="filesystem",
    )
