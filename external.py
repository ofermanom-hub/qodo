from typing import Optional

import requests

from utils import app_logger

_WEATHER_URL = "https://api.example.com/v1/weather"


def fetch_weather_hint(city: str) -> Optional[dict]:
    """Return a small dict like {'summary': '...'} or None on upstream failure.

    Callers MUST handle the None case — upstream is best-effort.
    """
    try:
        resp = requests.get(_WEATHER_URL, params={"city": city}, timeout=2.0)
        if resp.status_code >= 500:
            app_logger.warning("weather upstream 5xx for city=%s", city)
            return None
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        app_logger.warning("weather request failed: %s", exc)
        return None
