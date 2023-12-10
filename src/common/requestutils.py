import datetime
import logging
from typing import Optional

import requests
from requests_cache import CachedSession

logger = logging.getLogger(__name__)


def send_resquest(url, params=None, cache: Optional[CachedSession] = None):
    if cache:
        data = cache.get(
            url,
            params=params,
            # headers={"User-Agent": "Mozilla/5.0"},
        )
        if data.from_cache:
            logger.info(f"Using cached data for {url}")
            expires_seconds = data.created_at + datetime.timedelta(
                seconds=cache.expire_after
            )
            expires_seconds = expires_seconds - datetime.datetime.now()
            logger.info(f"Data expires in {expires_seconds} at {data.expires}")
        else:
            if data.status_code != 200:
                logger.warning(f"Status code {data.status_code} for {url}")
            else:
                logger.info(f"Got status code {data.status_code} for {url}")

    else:
        data = requests.get(
            url,
            params=params,
            # headers={"User-Agent": "Mozilla/5.0"},
        )
        logger.info(f"Got status code {data.status_code} for {url}")

    if data.status_code == 200:
        return data
    else:
        return None


def make_query_or(KEYWORDS):
    return " OR ".join([f'"{keyword}"' for keyword in KEYWORDS])


def make_query_and(KEYWORDS):
    return " AND ".join([f'"{keyword}"' for keyword in KEYWORDS])
